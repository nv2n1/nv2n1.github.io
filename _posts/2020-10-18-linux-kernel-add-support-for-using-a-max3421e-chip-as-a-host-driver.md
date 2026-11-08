---
title: "MAX3421E USB Host Driver for Linux Kernel"
date: 2020-10-18 04:49:29 +0000
modified: 2026-04-11 16:13:33 +0000
author: "Tony"
layout: post
categories: [linux-systems-administration]
canonical: /linux-kernel-add-support-for-using-a-max3421e-chip-as-a-host-driver/
---

The Linux kernel includes a USB host controller driver for the Maxim MAX3421E chip, which implements a USB 2.0 full-speed and low-speed host controller over SPI. This was introduced in commit 2d53139 by David Mosberger-Tang and is maintained in the kernel’s USB subsystem.

### Overview

The MAX3421E is a specialized chip that allows SPI-connected systems to function as USB hosts. Unlike traditional USB controllers that are memory-mapped or use dedicated buses, the MAX3421E communicates entirely through SPI transactions. This makes it useful for embedded systems, microcontrollers, and single-board computers where native USB host support isn’t available.

**Key capabilities:**

- USB 2.0 full-speed and low-speed host mode
- SPI interface (full-duplex mode)
- On-chip 64-byte FIFO for USB data transfers
- Support for control, interrupt, and bulk transfers
- Does not support isochronous transfers
- Typical power consumption: ~500mA at full load

### Driver Architecture

The driver (`drivers/usb/host/max3421-hcd.c`) uses a dedicated kernel thread (`max3421_spi_thread`) to handle all USB operations. This design is necessary because SPI transactions can sleep, which means they cannot be performed while holding spinlocks or with interrupts disabled.

**Threading model:**

- A hard interrupt handler (`max3421_irq_handler`) wakes the SPI thread when the chip needs attention
- The SPI thread processes all USB transfers, status changes, and frame numbering
- This separation ensures responsive interrupt handling while allowing blocking SPI calls

### Register Architecture

The MAX3421E uses a register-based interface. All register access goes through SPI with the format:

    [Command Byte] [Optional Data Bytes]

The command byte encodes the register address and direction (read/write). Key registers include:

- `MAX3421_REG_RCVFIFO` / `MAX3421_REG_SNDFIFO`: Data FIFOs
- `MAX3421_REG_HRSL`: Host result status (includes toggle bits and error codes)
- `MAX3421_REG_HXFR`: Host transfer command
- `MAX3421_REG_HIEN` / `MAX3421_REG_HIRQ`: Interrupt enable and status
- `MAX3421_REG_MODE`: Host mode configuration
- `MAX3421_REG_PERADDR`: Peripheral address (device address)

### Packet States and Transfer Flow

The driver models USB transfers as a state machine with three states:

1.  **PKT_STATE_SETUP**: Control transfers send an 8-byte SETUP packet
2.  **PKT_STATE_TRANSFER**: Data transfer phase (IN or OUT)
3.  **PKT_STATE_TERMINATE**: Handshake phase (completing control transfers)

Control transfers always follow: SETUP → TRANSFER (if data exists) → TERMINATE.

### Scheduling

The driver implements a two-pass scheduler running once per USB frame:

**SCHED_PASS_PERIODIC**: Handles interrupt and isochronous endpoints\
**SCHED_PASS_NON_PERIODIC**: Handles control and bulk endpoints

This ensures periodic transfers get priority while allowing bulk transfers to use remaining frame bandwidth. Each control endpoint is limited to one transaction per frame.

### Error Handling and Retries

The driver maps MAX3421E error codes (`HRSL` register) to standard Linux error codes:

- `MAX3421_HRSL_NAK`: Device not ready (retried up to `NAK_MAX_FAST_RETRANSMITS` times immediately, then once per frame)
- `MAX3421_HRSL_STALL`: Endpoint halted (returns `-EPIPE`)
- `MAX3421_HRSL_TIMEOUT`: Device timeout (returns `-ETIME`)
- `MAX3421_HRSL_BABBLE`: Device talked too long (returns `-EOVERFLOW`)
- CRC/packet errors: Retried up to `USB_MAX_RETRIES` times before reporting error

Toggle bit handling is automatic—the driver reads toggle state from `HRSL` and saves it per endpoint when switching to a new device.

### Configuration and Probe

The driver is registered as an SPI driver and probes compatible SPI devices:

``` c
static struct spi_driver max3421_driver = {
    .probe = max3421_probe,
    .remove = max3421_remove,
    .driver = {
        .name = "max3421-hcd",
        .owner = THIS_MODULE,
    },
};
```

During probe:

1.  Initialize the SPI bus
2.  Create a USB HCD structure
3.  Start the SPI thread
4.  Register the HCD with the USB core
5.  Request the IRQ line (typically low-active)

The probe function validates the chip revision (0x12 or 0x13) and logs SPI configuration details.

### Platform Data

The driver accepts platform data for GPIO control:

``` c
struct max3421_hcd_platform_data {
    u8 vbus_gpout; /* GPIO pin number (1-8) for VBUS control */
};
```

The `vbus_gpout` parameter specifies which MAX3421E GPIO output drives the VBUS power control. This allows automatic power management on the USB port.

### SPI Communication

All SPI operations use helper functions to abstract the transaction layer:

- `spi_rd8()`: Read single register
- `spi_wr8()`: Write single register
- `spi_rd_buf()`: Read buffer from FIFO
- `spi_wr_buf()`: Write buffer to FIFO

These functions handle proper SPI message formatting and use cache-aligned buffers to prevent DMA coherency issues.

### Known Limitations

- **No isochronous transfer support**: The 64-byte FIFO cannot accommodate isochronous packets larger than that size
- **Single device**: The driver doesn’t support hub operation; only one USB device can be connected
- **USB 2.0 full/low-speed only**: High-speed is not supported
- **Bus suspend/resume**: Not implemented (returns -1)

### Module Loading

Build as a module with `CONFIG_USB_MAX3421_HCD=m` or compile in with `CONFIG_USB_MAX3421_HCD=y`.

``` bash
modprobe max3421_hcd
```

The driver requires:

- `CONFIG_USB=y` or `=m`
- `CONFIG_SPI=y` or `=m`
- Proper device tree or platform data defining the SPI device

### Performance Considerations

SPI communication is the bottleneck. At typical SPI speeds (10-50MHz), full-speed USB performance can be achieved, but latency is higher than native controllers. The SPI thread runs at normal priority and can be preempted, which may cause occasional packet retransmissions under heavy system load.

For applications requiring predictable timing or very high throughput, consider using native USB controllers or dedicated hardware solutions instead of MAX3421E.
