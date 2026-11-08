---
title: "CalDAV and CardDAV: A Developer\u2019s Guide"
date: 2023-09-16 06:44:11 +0000
author: "Ethan Ainsworth"
layout: post
categories: [systems-architecture]
canonical: /caldav-and-carddav-101/
---

CalDAV and CardDAV are open, internet-based standards for syncing calendar and contact data across different devices and services. They’re built on WebDAV and the iCalendar/vCard formats, making them vendor-agnostic and suitable for both personal deployments and enterprise environments.

## What CalDAV Does

CalDAV handles calendar synchronization—events, tasks, reminders, and availability data. Add an event on your phone, and it propagates to your laptop, desktop, and any other connected client within seconds. CalDAV supports recurring events, timezone handling, free/busy information, and attendee management, making it suitable for everything from personal scheduling to shared team calendars.

## What CardDAV Does

CardDAV synchronizes contacts and address books. Update a phone number once on your primary device, and that change syncs to all clients. CardDAV stores contact data in vCard format, supporting complex fields like multiple phone numbers, addresses, organizations, photos, and custom properties.

## Why Run Your Own CalDAV/CardDAV Server

**Privacy and data control**: Unlike Google Calendar or Apple iCloud, hosting your own server keeps personal data on hardware you control. No algorithmic analysis, no data mining, no surprise policy changes.

**Interoperability across ecosystems**: CalDAV and CardDAV work natively on iOS, Android, Windows, macOS, and Linux. You’re not locked into a single vendor’s client ecosystem. Desktop applications like GNOME Evolution, Thunderbird, and KDE Kontact all support these protocols.

**Enterprise and team use**: Organizations need calendars and contacts that don’t depend on a third-party SaaS. CalDAV/CardDAV makes sense for internal deployments where you control the server and network.

## Common Server Options

**Nextcloud** remains the most popular choice for self-hosted CalDAV/CardDAV. It’s a full collaboration platform with web UI, mobile apps, and extensive third-party integrations.

**Radicale** is lightweight—a single Python application that requires minimal resources. Good for small deployments or systems with tight constraints.

**Baïkal** is a lightweight alternative with a simpler codebase than Nextcloud but more features than Radicale.

**Zimbra** and **EGroupware** are enterprise-grade, supporting CalDAV/CardDAV alongside email and other groupware features.

## Basic CalDAV/CardDAV URLs

Once your server is running, clients connect via simple URLs:

- CalDAV calendar: `https://your-domain.com/remote.php/dav/calendars/username/calendar-name/`
- CardDAV addressbook: `https://your-domain.com/remote.php/dav/addressbooks/username/contacts/`

These URLs are standardized across most servers. iOS and Android apps auto-discover them using DNS SRV records if configured properly.

## Client Setup Examples

**Desktop clients** (GNOME Evolution, Thunderbird):\
Enter the server URL and credentials. The client queries the `.well-known/caldav` and `.well-known/carddav` endpoints for auto-discovery.

**Mobile apps** (iOS Calendar/Contacts apps, Android’s built-in apps, or third-party options like Davx⁵):\
Use the calendar/contact settings, add account, select “CalDAV” or “CardDAV,” enter server URL and credentials.

**Syncing from Google Calendar or iCloud**:\
Import your existing calendars as `.ics` files into your server, or use tools like `vdirsyncer` to bridge your existing accounts with your CalDAV server.

## Important Considerations

**SSL/TLS is mandatory**: CalDAV/CardDAV transmit authentication credentials. Always use HTTPS with a valid certificate (Let’s Encrypt works fine). HTTP without encryption is a security liability.

**Timezone handling**: CalDAV supports multiple timezones in a single calendar. Ensure your server and clients handle VTIMEZONE blocks correctly, especially for recurring events across DST boundaries.

**Scalability**: Self-hosted servers work well for individuals and small teams (under 50 users). Larger deployments should consider load balancing, replication, and database optimization.

**Backup strategy**: Your calendar and contact data becomes critical. Automate regular backups, maintain offsite copies, and test restore procedures.

CalDAV and CardDAV aren’t new—they’ve been around for nearly two decades—but they’re increasingly relevant as organizations prioritize privacy and interoperability over convenience.
