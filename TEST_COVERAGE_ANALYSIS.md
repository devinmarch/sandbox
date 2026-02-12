# Test Coverage Analysis

## Current State: Zero Test Coverage

No tests, no test configuration, no testing dependencies exist in the codebase.

## Proposed Testing Areas (Prioritized by Risk)

### 1. Webhook Happy Paths (Critical)
- Room block created flow: Seam API call + DB record creation
- Room block removed flow: DB lookup + Seam API delete + DB record removal
- Mock `requests.post` to avoid hitting real Seam API

### 2. Webhook Error Handling (High)
- Unknown room ID → KeyError (no handling)
- Missing fields in webhook payload → KeyError
- Seam API failure on create (non-200 or malformed response)
- Seam API failure on delete (already returns 200 to caller)
- Empty `rooms` array → IndexError
- Room block removed but no DB record exists

### 3. Database Operations (Medium)
- CRUD operations on RoomBlockCode
- Query by block_id
- Duplicate block_id handling (no unique constraint exists)

### 4. Payload Filtering Logic (Medium)
- blockType must be `out_of_service`
- reason must be `guinness` (creation only)
- eventType filtering (`roomblock/created` vs `roomblock/removed` vs others)
- Case-insensitivity and whitespace trimming of reason field

### 5. Device ID Mapping (Low)
- All expected rooms present
- Each entry has `device_id` and `name` keys

## Setup Required
1. Add `pytest` to `requirements.txt`
2. Create `conftest.py` with test fixtures (in-memory DB, Flask test client)
3. Create `tests/` directory
4. Refactor `database.py` so the database can be swapped for testing
