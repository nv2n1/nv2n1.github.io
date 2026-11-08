---
title: "Fix clock validation in __pm_clk_add()"
date: 2020-10-01 01:50:57 +0000
author: "Tony"
layout: post
categories: [linux-systems-administration]
canonical: /linux-kernel-pm-clk-fix-clock-error-check-in-__pm_clk_add/
---

The `__pm_clk_add()` function in the Linux kernel handles clock registration for power management. A clock validation bug in this function could cause incorrect power state transitions or kernel warnings when managing device clocks.

## The Bug

The issue involved insufficient validation of clock pointers before adding them to the power management subsystem. When `__pm_clk_add()` received an invalid or NULL clock pointer under specific conditions, it could lead to:

- Kernel NULL pointer dereference panics
- Incorrect reference counting on clock handles
- Devices stuck in wrong power states after suspend/resume
- Warning traces in `dmesg` during boot or suspend cycles

## Affected Kernel Versions

The bug affected specific kernel versions in the power management clock framework. Check if your kernel is affected:

```wp-block-code
uname -r
# Check the kernel changelog for the specific patch
grep -r "pm_clk_add" /usr/src/linux/Documentation/
```

## The Fix

The patch adds proper NULL checks and validation before registering clocks with the PM subsystem:

```wp-block-code
/* Before fix (simplified) */
int __pm_clk_add(struct device *dev, const char *con_id, struct clk *clk)
{
    struct pm_clk_data *pcd = dev_to_pcd(dev);
    struct pm_clk_entry *ce;
    ce = kzalloc(sizeof(*ce), GFP_KERNEL);
    ce->clk = clk;  // No validation!
    list_add(&ce->node, &pcd->clock_list);
}

/* After fix */
int __pm_clk_add(struct device *dev, const char *con_id, struct clk *clk)
{
    struct pm_clk_data *pcd = dev_to_pcd(dev);
    struct pm_clk_entry *ce;

    if (!clk)  // Validate before use
        return -EINVAL;

    ce = kzalloc(sizeof(*ce), GFP_KERNEL);
    if (!ce)
        return -ENOMEM;

    ce->clk = clk;
    list_add(&ce->node, &pcd->clock_list);
    return 0;
}
```

## How to Apply the Patch

If you’re running an affected kernel and can’t upgrade immediately:

```wp-block-code
# Download the specific patch from kernel.org
wget https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/patch/?id=<commit-hash>

# Apply to your kernel source
cd /usr/src/linux
patch -p1 < patchfile.patch

# Rebuild and install
make modules_prepare
make M=drivers/base/power
sudo make modules_install
```

## Checking for Related Issues

If you’re experiencing power management issues, check the kernel log:

```wp-block-code
# Look for PM clock warnings
dmesg | grep -i "pm_clk\|clock.*add\|pm domain"

# Check for suspend/resume failures
dmesg | grep -i "suspend\|resume\|pm_op"

# Trace power management events
echo 1 > /sys/power/pm_trace
# Then suspend and check dmesg after resume
```

## Power Management Clock Framework Overview

The PM clock framework (`drivers/base/power/clock_ops.c`) manages device clocks during power state transitions:

- `pm_clk_add()` — Register a clock for PM management by connection ID
- `__pm_clk_add()` — Internal function to register a clock by pointer
- `pm_clk_remove()` — Unregister a clock from PM management
- `pm_clk_suspend()` — Disable all managed clocks during suspend
- `pm_clk_resume()` — Re-enable all managed clocks during resume

The framework ensures that device clocks are properly gated during suspend and restored during resume, preventing power leaks and ensuring correct device initialization after wakeup.

## When to Worry About This

This bug primarily affects:

- Embedded systems with complex clock trees
- ARM platforms using PM domain frameworks
- Systems with runtime PM enabled that frequently suspend/resume devices

If your system doesn’t use PM clock management or doesn’t see warnings in dmesg related to clocks, this specific bug is unlikely to affect you. The fix was included in upstream kernels and backported to stable branches.

## Testing Power Management After Patching

After applying kernel power management patches, verify proper behavior:

```wp-block-code
# Test suspend/resume cycle
sudo rtcwake -m mem -s 30    # Suspend to RAM for 30 seconds

# Test with all PM debug enabled
echo 1 | sudo tee /sys/power/pm_debug_messages
sudo systemctl suspend

# After resume, check for errors
dmesg | grep -i 'error\|fail\|warn' | grep -i pm

# Verify clocks are restored
cat /sys/kernel/debug/clk/clk_summary
```

For automated testing, use the `pm-test` suite:

```wp-block-code
# Install pm-utils test tools
sudo dnf install pm-utils      # Fedora
sudo apt install pm-utils      # Ubuntu

# Run suspend test with 10 cycles
sudo pm-suspend-hybrid --quirk-test-mode
```

## Related Kernel Subsystems

The PM clock framework interacts with several other kernel subsystems:

- **GenPD (Generic Power Domains)** — Manages power domains that group multiple devices
- **Runtime PM** — Dynamically powers devices on/off based on usage
- **CLK framework** — The underlying clock management that PM clocks build on
- **Device tree** — Clock definitions are often specified in device tree bindings

When debugging PM issues, check all these layers. A clock not being properly managed by `__pm_clk_add()` can cascade into device initialization failures after resume.
