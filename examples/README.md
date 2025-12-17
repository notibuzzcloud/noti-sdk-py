# Usage Examples for noti-sdk-py

This folder contains practical examples organized by categories to help you use the SDK.

## Configuration

Before running the examples, configure the environment variables:

```bash
export NOTI_URL="https://your_domain_notibuzz"
export NOTI_KEY="your_api_key"
export NOTI_SESSION_NAME="default"  # Session name to use
```

Or modify directly in each file:

```python
configure_client({
    'noti_url': 'https://your_domain_notibuzz',
    'noti_api_key': 'your_api_key'
})

session_name = os.getenv('NOTI_SESSION_NAME', 'default')
```

## Structure

Examples are organized in subdirectories according to API categories:

### 📁 Sessions
- `list_sessions.py` - List all sessions
- `get_session.py` - Get session information
- `get_session_me.py` - Get authenticated account information

### 👤 Profile
- `get_my_profile.py` - Get profile information
- `set_profile_name.py` - Update profile name
- `set_profile_status.py` - Update status (About)
- `set_profile_picture.py` - Update profile picture
- `delete_profile_picture.py` - Delete profile picture

### 💬 Chatting
- `send_text.py` - Send text message
- `send_image.py` - Send image
- `send_file.py` - Send file
- `send_voice.py` - Send voice note
- `send_video.py` - Send video
- `send_poll.py` - Send poll
- `send_location.py` - Send location
- `send_contact_vcard.py` - Send contact (vCard)
- `send_list.py` - Send interactive list
- `send_link_preview.py` - Send message with custom link preview
- `send_bulk_messages.py` - Bulk message sending
- `reaction.py` - Add/remove reaction
- `start_typing.py` / `stop_typing.py` - Start/stop typing status

### 📱 Status
- `status_text.py` - Create text status
- `status_image.py` - Create image status
- `status_voice.py` - Create voice status
- `status_video.py` - Create video status
- `status_delete.py` - Delete status

### 💬 Chats
- `list_chats.py` - List chats
- `get_messages.py` - Get chat messages
- `get_message.py` - Get a specific message
- `mark_read.py` - Mark messages as read
- `edit_message.py` - Edit message
- `delete_message.py` - Delete message
- `pin_message.py` - Pin/unpin message

### 📇 Contacts
- `get_contact.py` - Get contact information
- `check_exists.py` - Check if a number exists on WhatsApp
- `get_profile_picture.py` - Get profile picture
- `upsert.py` - Create/update contact

## Execution

To run an example:

```bash
# From the project root
python examples/sessions/list_sessions.py

# Or from the examples folder
cd examples
python sessions/list_sessions.py
```

## Important Notes

1. **Install SDK**: Make sure you've installed the SDK (`pip install -e .` for development)

2. **Environment variables**: Examples use:
   - `NOTI_URL` - Bridge URL (default: `'your_base_url'`)
   - `NOTI_KEY` - API Key (default: `your_api_key`)
   - `NOTI_SESSION_NAME` - Session name (default: `default`)

3. **Real IDs**: Replace example IDs (chatId, messageId, etc.) with real values from your account

4. **Errors**: All examples include basic error handling

## Next Steps

- Review the [complete documentation](../README.md)
- Check the [API reference](../README.md#api-reference)
- Read the [quick start guide](../QUICK_START.md)

