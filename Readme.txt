# Comparing Versions Project

## Overview
This project is designed to compare source and target versions of software components, validate email addresses, and send a summary email to recipients about the comparison status. It supports validating email domains, parsing version formats, and comparing version details from JSON files.

---

## Features
- **Email Validation**: Validates email addresses against a predefined list of domains.
- **Version Comparison**: Compares software component versions between a source and a target in a structured JSON file.
- **Summarization Email**: Sends a summary email to the recipients, indicating the success or failure of the comparison.
- **Unit Testing**: Comprehensive test cases to validate the functionality.

---

## Project Structure
### Directories & Files
```
.
├── Domains.json                  # Contains valid email domains.
├── enums.py                      # Enum class for status handling.
├── Job.py                        # Base class handling email validation and summarization email.
├── compare_source_target.py      # Inherits from Job. Handles version comparison.
├── json_file.json                # Example file with identical source and target versions.
├── unequal_versions.json         # Example file with unequal source and target versions.
├── bad_version_format.json       # Example file with incorrect version formats.
├── Test.py                       # Unit tests for the project.
├── main.py                       # Entry point of the application.
```

---

## Requirements
- Python 3.8 or above
- Modules: `enum`, `json`, `os`, `re`, `smtplib`, `unittest`, `email`, `logging`

---

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ahmadaw34/Tsofen.git
   ```

2. Update `Domains.json` with valid email domains if needed.

3. Configure the email sender credentials in `Job.py`:
   ```python
   self.__email_sender='your_email@gmail.com'
   self.__password = 'your_email_password' # Use an App Password for Gmail.
   ```

---

## Running the Application
To execute the main process:
```bash
python main.py
```

### Parameters in `main.py`
- `addresses_to_send_report`: List of recipient email addresses.
- `version_file_name`: JSON file containing source and target versions.
- `send_email`: Boolean flag to enable/disable sending summarization emails.

Example:
```python
addresses_to_send_report = 'ahmadaw@post.bgu.ac.il,briq@post.bgu.ac.il'
version_file_name='json_file.json'
send_email=True
```

---

## Testing
Run the unit tests to validate functionality:
```bash
python -m unittest Test.py
```

### Test Cases in `Test.py`
- **Valid Emails, Equal Versions**: Expects `Status.Success`.
- **Valid Emails, Unequal Versions**: Expects `Status.Failure`.
- **Invalid Emails, Equal Versions**: Expects an exception.
- **Invalid Emails, Unequal Versions**: Expects an exception.
- **Valid Emails, Bad Version Format**: Expects an exception.
- **Invalid Emails, Bad Version Format**: Expects an exception.

---

## JSON File Structure
### Example
```json
{
  "source": {
    "project_name": "southernco-prod",
    "remedy_stack_version": "44.11.221",
    "smart_apps_stack_version": "122.05.24"
  },
  "target": {
    "project_name": "southernco-prod",
    "remedy_stack_version": "44.11.221",
    "smart_apps_stack_version": "122.05.24"
  }
}
```

### Explanation
- **source**: Represents the current version details.
- **target**: Represents the target version details for comparison.
- **Keys ending with `_version`**: Versions to compare.

---

## Logging
Logs are configured in `Job.py` and provide detailed runtime information. Logs include:
- Validation messages for emails.
- Errors and exceptions during execution.
- Comparison results.

---

## Notes
- Always use an App Password for Gmail when setting `__password`.
- Customize the valid domains in `Domains.json` as per your requirements.
- Extend `compare_source_target.py` if new validation or comparison logic is required.

---

## License
This project is licensed under the [MIT License](LICENSE).

