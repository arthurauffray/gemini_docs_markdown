# Use this script to create a clone of the /docs or /api_reference
# directory with code snippets of only your
# language of choice.
#
# Gemini docs use heading-based language sections (### Python, ### JavaScript, etc.)
# with indented code blocks, rather than fenced code blocks with language tags.

import argparse
import shutil
import os
import re

# Default language(s) to filter for when not specified
DEFAULT_LANGUAGES = ['python', 'rest']

# Languages that are considered mutually exclusive "request" languages.
# If we keep one of these, we drop the others (unless they are the fallback).
# These correspond to the ### headings used in the Gemini docs.
EXCLUSIVE_LANGS = {
    'python', 'javascript', 'go', 'java', 'c#', 'rest', 'apps script'
}

# Mapping of common aliases to canonical heading names
LANG_ALIASES = {
    'py': 'python',
    'js': 'javascript',
    'node': 'javascript',
    'node.js': 'javascript',
    'typescript': 'javascript',
    'ts': 'javascript',
    'golang': 'go',
    'curl': 'rest',
    'csharp': 'c#',
    'dotnet': 'c#',
    '.net': 'c#',
    'apps_script': 'apps script',
    'appsscript': 'apps script',
}


def normalize_lang(lang):
    """Normalize a language name to its canonical form."""
    lower = lang.lower().strip()
    return LANG_ALIASES.get(lower, lower)


def get_heading_lang(line):
    """
    Returns the language of a heading line (### Language), or None if not a heading.
    Only matches level-3 headings (###) that correspond to known languages.
    """
    stripped = line.strip()
    match = re.match(r'^###\s+(.+)$', stripped)
    if match:
        heading_text = match.group(1).strip()
        normalized = normalize_lang(heading_text)
        if normalized in EXCLUSIVE_LANGS:
            return normalized
    return None


def get_file_languages(filepath):
    """
    Scans a markdown file and returns a set of all languages found as ### headings.
    """
    langs = set()
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            lang = get_heading_lang(line)
            if lang:
                langs.add(lang)
    return langs


def filter_file_content(filepath, target_langs):
    """
    Reads the file, keeps only the appropriate language sections, and overwrites the file.
    target_langs: a list of strings (e.g., ['python', 'rest'])

    Gemini docs format:
    - Language sections start with ### <Language> headings
    - Code is in indented blocks (4 spaces) below the heading
    - A section ends when the next heading of equal or higher level is found,
      or a non-indented, non-empty line that isn't part of the code block
    """
    # 1. Identify available languages
    available_langs = get_file_languages(filepath)

    # Normalize target languages
    target_lower_list = [normalize_lang(l) for l in target_langs]

    # 2. Determine Keep Strategy
    keep_langs = set()

    # Strategy:
    # - for each requested language in target_lower_list, if present in file, keep it.
    # - if NO requested language is present, check for 'rest' (curl).
    #   - if 'rest' is present, keep 'rest' (fallback).
    #   - otherwise, keep none of the exclusive languages.

    any_target_found = False
    for t_lang in target_lower_list:
        if t_lang in available_langs:
            keep_langs.add(t_lang)
            any_target_found = True

    if not any_target_found and 'rest' in available_langs:
        # Fallback to REST/curl if no target found
        keep_langs.add('rest')

    # Read content
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    filtered_lines = []
    skipping = False
    current_lang_section = None

    for i, line in enumerate(lines):
        lang = get_heading_lang(line)

        if lang is not None:
            # This is a language heading
            if lang in EXCLUSIVE_LANGS:
                if lang in keep_langs:
                    skipping = False
                    current_lang_section = lang
                else:
                    skipping = True
                    current_lang_section = lang
            else:
                skipping = False
                current_lang_section = None

            if not skipping:
                filtered_lines.append(line)
            continue

        # Check if we hit a non-language heading (##, ###, etc) which ends the current section
        # Markdown headings have at most 3 spaces before the #
        if re.match(r'^\s{0,3}#+\s+', line):
            # Any heading ends the current language section
            skipping = False
            current_lang_section = None
            filtered_lines.append(line)
            continue

        if not skipping:
            filtered_lines.append(line)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(filtered_lines)


def process_directory(source_dir, dest_dir, target_langs):
    # If dest_dir is None, filter in-place
    if dest_dir is None:
        if os.path.isfile(source_dir):
            # Filter single file in-place
            if source_dir.endswith('.md'):
                print(f"Filtering {source_dir} in-place...")
                filter_file_content(source_dir, target_langs)
                print("Processed 1 markdown file.")
            else:
                print("Source file is not a markdown file; no filtering applied.")
        else:
            # Filter directory in-place
            print(f"Filtering markdown files in {source_dir} in-place for languages: {target_langs}")
            count = 0
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    if file.endswith('.md'):
                        filepath = os.path.join(root, file)
                        filter_file_content(filepath, target_langs)
                        count += 1
            print(f"Processed {count} markdown files.")
        return

    # If source is a file, copy just that file and filter it.
    if os.path.isfile(source_dir):
        # Determine destination file path
        if os.path.isdir(dest_dir):
            dest_file = os.path.join(dest_dir, os.path.basename(source_dir))
        else:
            dest_parent = os.path.dirname(dest_dir)
            if dest_parent:
                os.makedirs(dest_parent, exist_ok=True)
            dest_file = dest_dir

        if os.path.exists(dest_file):
            print(f"Destination {dest_file} already exists. Overwriting...")
        else:
            print(f"Copying file {source_dir} to {dest_file}...")

        shutil.copy2(source_dir, dest_file)

        if dest_file.endswith('.md'):
            filter_file_content(dest_file, target_langs)
            print("Processed 1 markdown file.")
        else:
            print("Source file copied but not a markdown file; no filtering applied.")

        return

    # Otherwise assume source is a directory: copy entire directory structure
    if os.path.exists(dest_dir):
        print(f"Destination {dest_dir} already exists. Removing it to start fresh...")
        shutil.rmtree(dest_dir)

    print(f"Copying {source_dir} to {dest_dir}...")
    shutil.copytree(source_dir, dest_dir)

    # Walk through destination and filter .md files
    print(f"Filtering markdown files for languages: {target_langs}")
    count = 0
    for root, dirs, files in os.walk(dest_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                filter_file_content(filepath, target_langs)
                count += 1

    print(f"Processed {count} markdown files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy Gemini docs and filter code snippets by language.")
    # Positional source allows calling: python filter_docs.py docs/file.md
    parser.add_argument('pos_source', nargs='?', help='Positional source file or directory (optional alternative to -s)')
    parser.add_argument("--source", "-s", dest='opt_source', help="Source file or directory (e.g. docs or docs/file.md)")
    parser.add_argument("--destination", "-d", default=None, help="Destination file or directory (optional; if not provided, filters in-place)")
    parser.add_argument("--languages", "-l", nargs='+', default=DEFAULT_LANGUAGES, help=f"Target languages (e.g. python javascript). Default: {DEFAULT_LANGUAGES}")

    args = parser.parse_args()

    # Choose source: positional overrides if present, otherwise use -s/--source
    source = args.pos_source if args.pos_source else args.opt_source
    if not source:
        parser.error('a source is required (positional or --source/-s)')

    process_directory(source, args.destination, args.languages)
