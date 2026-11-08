---
title: "Optimizing Firefox Performance on Linux"
date: 2013-07-12 16:32:03 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/speeding-up-firefox-on-linux/
---

Firefox performance on Linux can be significantly improved through configuration tuning. Most of these settings apply across platforms, though this guide focuses on Linux-specific considerations.

## Network Pipelining

HTTP pipelining allows Firefox to send multiple requests on a single connection before waiting for responses. Modern HTTP/2 and HTTP/3 handle multiplexing more efficiently, but pipelining can still help with some servers.

Access the Firefox configuration editor:

1.  Type `about:config` in the address bar
2.  Accept the warning about voiding warranty
3.  Modify these settings:
    - `network.http.pipelining`: set to `true`
    - `network.http.proxy.pipelining`: set to `true`
    - `network.http.pipelining.maxrequests`: set to `25` (adjust based on your network conditions; higher values like 50 can help with high-latency connections but may impact stability)

Note that some servers don’t handle pipelining well. If you experience connection issues, revert these changes.

## Initial Paint Delay

Firefox waits briefly before rendering page content. Reducing this delay makes pages feel snappier, especially on fast connections.

In `about:config`:

1.  Right-click the preference list
2.  Select **New** → **Integer**
3.  Create `nglayout.initialpaint.delay` and set it to `0`

This eliminates the render delay. Set it higher (50-100ms) if you experience visual glitches.

## Memory-Based Caching

If you have 2GB+ RAM, you can cache Firefox data in RAM (`/dev/shm`) instead of disk. This reduces disk I/O but uses system memory.

In `about:config`:

1.  Right-click the preference list
2.  Select **New** → **String**
3.  Create `browser.cache.disk.parent_directory` and set it to `/dev/shm/ffcache`

Firefox will create its cache structure in `/dev/shm/ffcache/Cache`. On systems with limited RAM or SSD storage, this may not provide noticeable benefits. If performance degrades, delete this preference to revert to disk caching.

For persistence across reboots on systems using `/dev/shm`, consider adding to your startup scripts:

``` bash
mkdir -p /dev/shm/ffcache
chmod 700 /dev/shm/ffcache
```

## DNS and IPv6

Slow DNS resolution can bottleneck browsing. If you don’t use IPv6, disabling it in Firefox can improve DNS performance:

In `about:config`:

- `network.dns.disableIPv6`: set to `true`

To disable IPv6 at the system level on Linux (optional), modify your kernel boot parameters. On systems using GRUB:

``` bash
sudo nano /etc/default/grub
```

Add `ipv6.disable=1` to the `GRUB_CMDLINE_LINUX` line:

    GRUB_CMDLINE_LINUX="... ipv6.disable=1"

Then rebuild the GRUB configuration:

``` bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

Reboot to apply. Alternatively, disable IPv6 at runtime with:

``` bash
echo "net.ipv6.conf.all.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.d/99-disable-ipv6.conf
sudo sysctl -p /etc/sysctl.d/99-disable-ipv6.conf
```

## Additional Performance Tuning

**Reduce extensions and themes**: Each extension consumes memory and CPU. Disable unused ones via `about:addons`.

**Hardware acceleration**: Ensure it’s enabled for GPU rendering in **Settings** → **General** → **Performance**. Modern systems benefit significantly from this.

**Content sandbox security level**: In `about:config`, `security.sandbox.content.level` can be reduced for performance at the cost of security (not recommended for most users).

**Deferring background tabs**: Set `browser.sessionstore.interval` to `30000` (milliseconds) to reduce background tab resource usage.

**Disable prefetching**: If your connection is metered, disable `network.prefetch-next` and `network.dns.disablePrefetch`.

## Profile Maintenance

Periodically clean your Firefox profile to remove accumulated cache and temporary data:

``` bash
rm -rf ~/.cache/mozilla/firefox/*/cache2
```

For a more aggressive cleanup of your profile while Firefox is closed:

``` bash
firefox --profile ~/.mozilla/firefox/YOUR_PROFILE_NAME -offline
```

Then restart normally. Be cautious with profile manipulation—always back up before major changes.

These optimizations work best in combination. Start with the DNS and initial paint delay settings, then experiment with network and caching settings to find what works best for your hardware and network conditions.
