# 0x02. i18n

## Description

This project introduces the concept of internationalization (i18n) in Flask web applications. The goal is to build a web app that supports multiple languages and handles locale-based formatting like time zones and messages.

## Learning Objectives

- Understand how to parametrize Flask templates to support multiple languages
- Infer locale from URL parameters, user settings, and request headers
- Localize timestamps and timezones using `pytz`

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- PEP8 style (`pycodestyle` 2.5)
- All Python files must be executable and start with `#!/usr/bin/env python3`
- All modules, classes, and functions must be documented with complete sentences
- Use type annotations
- Include a `README.md` at the root of the project

## Project Structure

- `0-app.py` - Basic Flask app setup with a route and template
- `1-app.py` - Flask-Babel configuration with language support
- `2-app.py` - Language detection from request headers
- `3-app.py` - Parametrized templates using translation files
- `4-app.py` - Locale override via URL parameter
- `5-app.py` - Mock user login using URL parameter
- `6-app.py` - Use logged-in user's preferred locale
- `7-app.py` - Infer and validate timezone with fallback

## Translations

Supports English (`en`) and French (`fr`). Message IDs are used for dynamic translation in templates.

## Testing

- Visit `/` for default language
- Use `?locale=fr` to switch to French
- Use `?login_as=1` to simulate user login
- Combine parameters to test priority logic (locale and login)

