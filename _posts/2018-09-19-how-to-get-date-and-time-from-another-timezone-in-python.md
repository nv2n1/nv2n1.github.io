---
title: "Choosing Between Python\u2019s zoneinfo and pytz"
date: 2018-09-19 04:48:56 +0000
layout: post
canonical: https://www.systutorials.com/how-to-get-date-and-time-from-another-timezone-in-python/
---

Python’s standard library includes `zoneinfo`, which handles timezones correctly without external dependencies. Use it for all new code.

``` python
from datetime import datetime
from zoneinfo import ZoneInfo

utc_time = datetime.now(ZoneInfo("UTC"))
ny_time = utc_time.astimezone(ZoneInfo("America/New_York"))
print(ny_time)
```

This automatically manages Daylight Saving Time transitions. The IANA timezone database (via the `tzdata` package on Windows; built-in on Unix-like systems) backs the lookups, so timezone rules stay current as DST rules change.

## Creating Timezone-Aware Datetimes

You’ll often need to create a datetime in a specific timezone rather than convert from UTC:

``` python
from datetime import datetime
from zoneinfo import ZoneInfo

# Create a datetime in Tokyo timezone
tokyo_tz = ZoneInfo("Asia/Tokyo")
meeting_time = datetime(2026, 6, 15, 14, 30, tzinfo=tokyo_tz)
print(meeting_time)
# 2026-06-15 14:30:00+09:00

# Convert to your local timezone
local_tz = ZoneInfo("America/Chicago")
local_meeting = meeting_time.astimezone(local_tz)
print(local_meeting)
# 2026-06-15 00:30:00-05:00
```

The key difference: passing `tzinfo` directly to the constructor creates a datetime in that timezone, while `astimezone()` converts an existing datetime.

## Converting Between Timezones

When working with multiple timezones, always use `astimezone()` to convert:

``` python
from datetime import datetime
from zoneinfo import ZoneInfo

# Start with a UTC time
utc_time = datetime(2026, 3, 10, 12, 0, tzinfo=ZoneInfo("UTC"))

# Convert to different timezones
london = utc_time.astimezone(ZoneInfo("Europe/London"))
sydney = utc_time.astimezone(ZoneInfo("Australia/Sydney"))
mumbai = utc_time.astimezone(ZoneInfo("Asia/Kolkata"))

print(f"UTC: {utc_time}")
print(f"London: {london}")
print(f"Sydney: {sydney}")
print(f"Mumbai: {mumbai}")
```

All conversions reference the same instant in time — only the local representation changes.

## Handling DST Transitions

The `zoneinfo` library handles DST automatically, but you need to be aware of ambiguous times during transitions. When clocks “fall back,” a time exists twice:

``` python
from datetime import datetime
from zoneinfo import ZoneInfo

# During DST transition, 1:30 AM occurs twice
# zoneinfo defaults to the first occurrence (fold=0)
eastern = ZoneInfo("America/New_York")

# First occurrence (EDT, UTC-4)
time1 = datetime(2026, 11, 1, 1, 30, fold=0, tzinfo=eastern)
print(time1)  # 2026-11-01 01:30:00-04:00

# Second occurrence (EST, UTC-5)
time2 = datetime(2026, 11, 1, 1, 30, fold=1, tzinfo=eastern)
print(time2)  # 2026-11-01 01:30:00-05:00
```

Use `fold=0` for the first occurrence and `fold=1` for the second. If users specify an ambiguous time, validate and handle it explicitly rather than silently picking the wrong one. You can check if a time is ambiguous:

``` python
from datetime import datetime
from zoneinfo import ZoneInfo

def is_ambiguous(dt):
    """Check if a naive datetime is ambiguous in the given timezone."""
    tz = dt.tzinfo
    # If fold=0 and fold=1 produce different offsets, the time is ambiguous
    dt_fold0 = dt.replace(fold=0)
    dt_fold1 = dt.replace(fold=1)
    return dt_fold0.utcoffset() != dt_fold1.utcoffset()

eastern = ZoneInfo("America/New_York")
ambig_time = datetime(2026, 11, 1, 1, 30, tzinfo=eastern)
print(is_ambiguous(ambig_time))  # True
```

## Database Best Practices

Store all timestamps in UTC in your database. Convert to the user’s local timezone only when displaying:

``` python
from datetime import datetime
from zoneinfo import ZoneInfo

# Save to database as UTC
def save_event(event_name, local_datetime_str, user_timezone_str):
    user_tz = ZoneInfo(user_timezone_str)
    local_dt = datetime.fromisoformat(local_datetime_str).replace(tzinfo=user_tz)
    utc_dt = local_dt.astimezone(ZoneInfo("UTC"))

    # Store utc_dt.isoformat() in your database
    return utc_dt.isoformat()

# Retrieve from database and convert to user timezone
def display_event(utc_datetime_str, user_timezone_str):
    utc_dt = datetime.fromisoformat(utc_datetime_str)
    user_tz = ZoneInfo(user_timezone_str)
    user_dt = utc_dt.astimezone(user_tz)

    return user_dt.strftime("%Y-%m-%d %H:%M:%S %Z")

# Example usage
event_utc = save_event("Team standup", "2026-06-15T09:00:00", "America/Denver")
display_event(event_utc, "Europe/Berlin")
# 2026-06-15 17:00:00 CEST
```

This approach ensures consistency across your system. Avoid storing timezone information with datetimes in the database — the timezone offset can change due to DST rule updates, making historical data unreliable.

## Getting the Current Time in a Specific Timezone

For real-time queries without conversion:

``` python
from datetime import datetime
from zoneinfo import ZoneInfo

# Current time in Tokyo (right now, not converted)
tokyo_now = datetime.now(ZoneInfo("Asia/Tokyo"))
print(tokyo_now)

# Current time in UTC
utc_now = datetime.now(ZoneInfo("UTC"))
print(utc_now)
```

## Python 3.8 and Earlier: Using pytz

If you’re stuck on Python 3.8, use the `pytz` library:

``` python
from datetime import datetime
import pytz

ny_tz = pytz.timezone("America/New_York")
ny_time = datetime.now(ny_tz)
print(ny_time)
```

However, `pytz` requires explicit localization and is more error-prone with DST:

``` python
import pytz
from datetime import datetime

eastern = pytz.timezone("America/New_York")

# Wrong way (naive datetime won't handle DST correctly)
wrong = datetime(2026, 6, 15, 14, 30, tzinfo=eastern)

# Right way (use localize)
correct = eastern.localize(datetime(2026, 6, 15, 14, 30))
```

**Upgrade to Python 3.9+ if possible** — `zoneinfo` is simpler and doesn’t require workarounds.

## Avoiding Common Pitfalls

**Never use naive datetimes in production code:**

``` python
# DON'T DO THIS
naive_time = datetime.now()  # No timezone info — ambiguous

# DO THIS
aware_time = datetime.now(ZoneInfo("UTC"))  # Always timezone-aware
```

Naive datetimes cause subtle bugs when code runs in different environments or processes events from multiple timezones. If you receive a naive datetime from an external source, always attach timezone info before using it:

``` python
from datetime import datetime
from zoneinfo import ZoneInfo

# Data from an API with no timezone info
api_time_str = "2026-06-15T14:30:00"
naive_dt = datetime.fromisoformat(api_time_str)

# Assume it's in the user's timezone (don't assume UTC unless documented)
user_tz = ZoneInfo("America/Los_Angeles")
aware_dt = naive_dt.replace(tzinfo=user_tz)

# Now safe to use
utc_dt = aware_dt.astimezone(ZoneInfo("UTC"))
```
