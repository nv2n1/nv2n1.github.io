---
title: "Understanding Xen\u2019s Codebase Architecture"
date: 2013-07-12 16:32:18 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /a-introduction-to-xen-source-code-structure-and-disk-in-xen/
---

Xen remains a production hypervisor used by AWS EC2, Citrix Hypervisor, and other cloud providers, though most general-purpose Linux distributions have shifted toward KVM as their default. If you’re working with Xen in production or developing drivers, understanding its source code layout is essential.

## Top-Level Directory Structure

The Xen source repository (hosted on xenbits.xen.org) is organized into these primary directories:

**docs/** — Documentation, man pages, and design specifications. These have evolved significantly; modern docs cover PVH (Paravirtualized with Hardware extensions) mode and newer security features.

**tools/** — Management utilities including `xl` (the modern tool replacing deprecated `xm`), `xentop` for monitoring, libxl for domain management, and libxenstore for configuration store access.

**xen/** — The hypervisor core, written primarily in C with assembly for architecture-specific operations.

**linux/** or **linux-xxx-xen/** — Paravirtualized Linux kernel source with Xen support. Modern versions patch upstream Linux directly rather than maintaining separate kernel trees.

**extras/** — Optional utilities and experimental features.

**stubdom/** — Stub domain implementations for enhanced isolation (e.g., MiniOS-based domains providing backend services).

## Core Hypervisor Layout (xen/)

Inside the hypervisor source directory:

**common/** — Shared hypervisor functionality: domain management, scheduler, memory management, event channels, and grant tables. Code here runs in the Xen runtime context.

**arch/** — Architecture-specific implementations for x86, x86-64, and ARM64. Includes boot code, paging, interrupt handlers, and CPU features detection.

**drivers/** — Backend drivers (disk, network, USB, IOMMU management). These handle physical device access and run with dom0 privileges.

**xsm/** — Xen Security Modules implementing mandatory access control (MAC). The FLASK security policy engine is the primary implementation; others include dummy (no policy) and ACM (deprecated).

**include/** — Header files defining interfaces between hypervisor components and between hypervisor and guest kernels.

**tools/** — Hypervisor build utilities and low-level domain management tools like `xenstore-clients` and event channel utilities.

## Backend and Frontend Driver Architecture

The split-driver model is Xen’s mechanism for safe device virtualization. Frontend and backend drivers communicate through shared memory, eliminating the need for hypervisor involvement in data-path operations.

**Backend drivers** run in dom0 (Domain 0, the management domain) and provide access to real hardware:

- Implemented as Linux kernel modules or as stub domains
- Handle physical disk, network, USB, and other I/O devices
- Expose a virtual interface through XenBus
- Manage grant tables and shared ring buffers for data transfer

**Frontend drivers** run in guest domains (domU) and interface with virtual devices:

- Implemented as drivers in the guest OS kernel or userspace via PV backends
- Present standard block/net device abstractions to guest applications
- Use xenstore for configuration and XenBus for initialization
- Access shared memory via grant references without hypervisor mediation

**XenBus** is the out-of-band control path—a shared memory region and event channel mechanism allowing frontend/backend negotiation. State machines govern device initialization: Initialising → InitWait → Initialised → Connected.

**XenStore** is a key-value database accessible from all domains, storing device configuration, domain metadata, and runtime parameters. The daemon `xenstore-read` and `xenstore-write` tools allow query access.

**Grant tables** allow domains to grant other domains access to specific memory pages without copying. Backend drivers use grants to safely read/write guest buffers.

## Practical Development Workflow

When modifying Xen:

- Edit hypervisor code in `xen/arch` or `xen/common`
- Build with `./configure && make world`
- For backend drivers, kernel modules go in dom0’s Linux kernel tree
- For frontend drivers, integrate into guest kernel or implement in userspace via `libxenlight`
- Test using `xl create` to start domains and monitor with `xl list` and `/proc/xen` interfaces

Modern Xen prefers PVH (Paravirtualized with Hardware extensions) mode, reducing code surface and improving compatibility. MiniOS stub domains isolate backend drivers from dom0 kernel, enhancing security—check `stubdom/` for examples.

For ongoing development, monitor the `xen-devel` mailing list and the Xen Project GitHub repository, as the codebase has modernized considerably since 2013.
