---
title: "fi_direct(7)"
name: "fi_direct"
section: "7"
letter: "f"
url: "/docs/linux/man/7-fi_direct/"
---

fi_direct - Direct fabric provider access

<h2>Synopsis</h2>

<pre><code>-DFABRIC_DIRECT

#define FABRIC_DIRECT</code></pre> Fabric direct provides a mechanism for applications to compile against a specific fabric providers without going through the libfabric framework or function vector tables. This allows for extreme optimization via function inlining at the cost of supporting multiple providers or different versions of the same provider.

<h2>Description</h2>

The use of fabric direct is intended only for applications that require the absolute minimum software latency, and are willing to re-compile for specific fabric hardware. Providers that support fabric direct implement their own versions of the static inline calls which are define in the libfabric header files, define selected enum values, and provide defines for compile-time optimizations. Applications can then code against the standard libfabric calls, but link directly against the provider calls by defining FABRIC_DIRECT as part of their build. 

 In general, the use of fabric direct does not require application source code changes, and, instead, is limited to the build process. 

 Providers supporting fabric direct must install 'direct' versions of all libfabric header files. For convenience, the libfabric sources contain sample header files that may be modified by a provider. The 'direct' header file names have 'fi_direct' as their prefix: fi_direct.h, fi_direct_endpoint.h, etc. 

 Direct providers are prohibited from overriding or modifying existing data structures. However, provider specific extensions are still available. In addition to provider direct function calls to provider code, a fabric direct provider may define zero of more of the following capability definitions. Applications can check for these capabilities in order to optimize code paths at compile time, versus relying on run-time checks.

<h2>Capability Definitions</h2>

In order that application code may be optimized during compile time, direct providers must provide definitions for various capabilities and modes, if those capabilities are supported. The following #define values may be used by an application to test for provider support of supported features. 

 FI_DIRECT_CONTEXT : The provider sets FI_CONTEXT or FI_CONTEXT2 for fi_info:mode. See fi_getinfo for additional details. When FI_DIRECT_CONTEXT is defined, applications should use struct fi_context in their definitions, even if FI_CONTEXT2 is set. 

 FI_DIRECT_LOCAL_MR : The provider sets FI_LOCAL_MR for fi_info:mode. See fi_getinfo for additional details.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-fi_getinfo/">fi_getinfo</a>(3), <a HREF="/docs/linux/man/3-fi_endpoint/">fi_endpoint</a>(3), <a HREF="/docs/linux/man/3-fi_domain/">fi_domain</a>(3)

<h2>Authors</h2>

OpenFabrics.
