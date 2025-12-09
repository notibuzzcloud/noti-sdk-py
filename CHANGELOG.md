# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-XX

### Added
- Initial release
- Complete Python SDK for NotiBuzz Bridge
- Support for all Bridge endpoints:
  - Sessions management
  - Profile management
  - Chatting (text, image, file, voice, video, poll, location, contact, forward)
  - Status/Stories (text, image, voice, video, delete)
  - Chats management (overview, messages, read, edit, pin, archive)
  - Contacts management
- Bulk messaging support with anti-ban controls
- Async message queuing
- Campaign control (stop, resume, availability check)
- Comprehensive documentation
- Examples for common use cases
- Automatic suppression of urllib3 OpenSSL warnings (macOS compatibility)

### Features
- Full Python support with type hints
- Clean and intuitive API
- Async/await support (via async_ parameter)
- Error handling with requests exceptions
- Request/response type safety
- Environment variable configuration support

