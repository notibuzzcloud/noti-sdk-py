# Quick Start - Test the SDK Locally

## Quick Steps

### 1. Install the SDK in development mode

```bash
cd noti-sdk-py
pip install -e .
```

### 2. Configure environment variables

```bash
export NOTI_URL="https://your-bridge-url.com"
export NOTI_KEY="your_api_key"
export NOTI_SESSION_NAME="default"
```

Or create a `.env` file:

```bash
cat > .env << EOF
NOTI_URL=https://your-bridge-url.com
NOTI_KEY=your_api_key
NOTI_SESSION_NAME=default
EOF

# Load variables
export $(cat .env | xargs)
```

### 3. Run an example

```bash
# List sessions
python examples/list_sessions.py

# Send message (change chat_id first)
python examples/send_text.py
```

### 4. Or use the helper script

```bash
chmod +x run_example.sh
./run_example.sh list_sessions
```

## Verify Installation

```bash
python -c "from noti_sdk_py import configure_client; print('✅ OK')"
```

## Quick Troubleshooting

| Error | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -e .` |
| `API Key is required` | Configure `NOTI_URL` and `NOTI_KEY` |
| `HTTP 401` | Verify that your API Key is correct |

For more details, see [TESTING.md](TESTING.md)
