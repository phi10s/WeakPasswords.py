# WeakPasswords.py

This script generates probable weak passwords for password spraying based on the current season and date, with optional parameters for customizing the output, including the addition of company names, other names (e.g. local sports teams, company addresses, etc.), and a specification of a minimum length for the resulting output to align with known password policies. 

## Features

- Generates weak passwords using common patterns and current date.
- Allows inclusion of a company name or other names in the generated passwords.
- Optionally includes thorough combinations of company name, month prefix, and suffix.
- Filters passwords based on a specified minimum length.

## Usage

### Command Line Arguments

- `-c`, `--company`: Optional company name to include in passwords.
- `-t`, `--thorough`: Include thorough combinations of company name, month prefix, and suffix.
- `-n`, `--names`: List of other names to include in passwords.
- `-m`, `--min_length`: Minimum length of the output passwords.

### Example

```bash
python WeakPasswords.py -c AcmeCorp -t -n John Doe -m 12
```

This command generates weak passwords that include "AcmeCorp", "John", and "Doe" with thorough combinations, and only outputs passwords that are 12 characters or longer.

## Output

The script prints the generated passwords to the console and writes them to a file named `latest_passwords.txt`.

## Acknowledgements

This script is based on `weakpass_generator.py` by nyxgeek (@nyxgeek) . The original script can be found [here](https://github.com/nyxgeek/weakpass_generator).

