---
title: "An Introduction to Xen\u2019s paravirt_ops Interface"
date: 2013-07-12 16:32:20 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/simple-introduction-to-paravirt_ops-for-xen/
---

paravirt_ops is an abstraction layer in the Linux kernel that allows the same binary to run efficiently on both bare metal and various hypervisors through runtime patching. Rather than compiling separate kernels for each platform, paravirt_ops lets the kernel detect its environment at boot and optimize itself accordingly.

## The Core Problem paravirt_ops Solves

Traditional virtualization requires the hypervisor to trap and emulate privileged CPU instructions. This is expensive. Paravirtualization offers a better approach: the guest OS cooperates with the hypervisor through well-defined hypercalls instead of instruction emulation.

However, supporting both bare metal and multiple hypervisors in a single kernel creates a challenge. You can’t simply call different hypercalls at compile time — you need runtime selection.

paravirt_ops addresses this by providing a set of function pointers for privileged operations. At boot, the kernel detects which environment it’s running in (bare metal, Xen, KVM, Hyper-V, etc.) and fills in the appropriate implementations.

## How paravirt_ops Works: A Concrete Example

Consider interrupt handling. On bare metal, disabling interrupts is a single instruction:

``` c
// Bare metal implementation
static inline void raw_local_irq_disable(void)
{
    asm volatile("cli" ::: "memory");
}
```

Under Xen, direct `cli` instructions fail. Instead, you must hypercall into Xen:

``` c
// Xen implementation
static inline void xen_irq_disable(void)
{
    struct vcpu_info *vcpu = this_cpu_read(xen_vcpu);
    vcpu->evtchn_upcall_mask = 1;
}
```

With paravirt_ops, the kernel abstracts this difference. The actual implementation chosen at runtime:

``` c
// Abstracted version
#define raw_local_irq_disable() PVOP_VCALL0(irq_disable)
```

`PVOP_VCALL0` is a macro that calls the function pointer installed during boot. On bare metal, it points to the `cli` instruction. On Xen, it points to the Xen hypercall.

## The paravirt_ops Structure

The kernel maintains a `paravirt_ops` structure containing function pointers for critical operations:

``` c
struct paravirt_ops {
    unsigned int kernel_rpl;
    unsigned int guest_type;
    unsigned int guest_features;
    unsigned long (*get_wallclock)(void);
    unsigned long (*set_wallclock)(unsigned long);
    void (*cpuid)(unsigned int *eax, unsigned int *ebx,
                  unsigned int *ecx, unsigned int *edx);
    unsigned long (*get_tsc)(void);
    // ... many more function pointers
};
```

Each field points to a hypervisor-specific or bare-metal implementation.

## Runtime Patching

paravirt_ops also uses a clever runtime patching mechanism. At compile time, common operations like `raw_local_irq_disable()` are compiled to an indirect call through a function pointer. During boot, the kernel can patch these calls with direct instructions if running on bare metal, eliminating the overhead.

This is done through specially-marked code sections that the bootloader inspects:

``` c
#define PVOP_CALL0(rettype, op)                         \
    ({ rettype __ret;                                    \
       unsigned long __eax = __LINE__;                   \
       asm volatile(paravirt_alt_call                    \
                    : "=a" (__eax) : [paravirt_op] "i" (&op)); \
       __ret = (rettype)__eax; __ret; })
```

## Current State of Paravirtualization

While Xen remains critical in certain environments (AWS EC2, Citrix), the Linux ecosystem has largely shifted:

- **KVM**: Now the default hypervisor for most Linux distributions. Includes paravirt_ops support via PV spinlocks and clock sources.
- **Hyper-V**: Microsoft’s hypervisor includes paravirt_ops implementations.
- **QEMU/KVM**: Supports enlightenments (paravirtualized features) for better performance.
- **Cloud platforms**: AWS uses Xen but provides Nitro instances (custom hypervisor). Azure, GCP, and others prefer KVM-based solutions.

## Practical Implications

If you’re building kernels for production:

- For cloud instances, check your provider’s documentation. AWS Xen instances benefit from Xen paravirt_ops. Nitro instances need different tuning.
- For on-premises virtualization, KVM is standard on RHEL/CentOS/Ubuntu.
- For containers (Docker, Kubernetes), paravirt_ops is irrelevant — containers share the host kernel.

## Checking Your Environment

Detect whether paravirt_ops is active:

``` bash
cat /proc/cpuinfo | grep -i hypervisor
dmesg | grep -i "paravirt"
cat /sys/devices/virtual/dmi/id/sys_vendor
```

On Xen, you’ll see `xen` in cpuinfo flags. On KVM, `kvm` appears. For details on running kernel code:

``` bash
sudo cat /sys/hypervisor/type
```

paravirt_ops remains an important optimization technique for virtualized kernels, enabling efficient cooperation between guest and hypervisor while maintaining kernel binary compatibility across platforms.
