---
title: "miniupnpc(3)"
name: "miniupnpc"
section: "3"
letter: "m"
url: "/docs/linux/man/3-miniupnpc/"
---

<h2>NAME</h2>

 miniupnpc - UPnP client library

<h2>SYNOPSIS</h2>

<h2>DESCRIPTION</h2>

 The miniupnpc library implement the UPnP protocol defined to dialog with Internet Gateway Devices. It also has the ability to use data gathered by <a HREF="/docs/linux/man/1-minissdpd/">minissdpd</a>(1) about UPnP devices up on the network in order to skip the long UPnP device discovery process. 

 At first, <a HREF="/docs/linux/man/3-upnpdiscover/">upnpDiscover</a>(3) has to be used to discover UPnP IGD present on the network. Then <a HREF="/docs/linux/man/3-upnp_getvalidigd/">UPNP_GetValidIGD</a>(3) to select the right one. Alternatively, <a HREF="/docs/linux/man/3-upnp_getigdfromurl/">UPNP_GetIGDFromUrl</a>(3) could be used to bypass discovery process if the root description url of the device to use is known. Then all the UPNP_* functions can be used, such as <a HREF="/docs/linux/man/3-upnp_getconnectiontypeinfo/">UPNP_GetConnectionTypeInfo</a>(3), <a HREF="/docs/linux/man/3-upnp_addportmapping/">UPNP_AddPortMapping</a>(3), etc...

<h2>HEADER FILES</h2>

<dl>
<dt>miniupnpc.h
<dd> That's the main header file for the miniupnpc library API. It contains all the functions and structures related to device discovery.
<dt>upnpcommands.h
<dd> This header file contain the UPnP IGD methods that are accessible through the miniupnpc API. The name of the C functions are matching the UPnP methods names. ie: GetGenericPortMappingEntry is UPNP_GetGenericPortMappingEntry.</dl>

<h2>API FUNCTIONS</h2>

<dl>
<dt>struct UPNPDev * upnpDiscover(int delay, const char * multicastif, const char * minissdpdsock, int localport, int ipv6, int * error);
<dd> execute the discovery process. delay (in millisecond) is the maximum time for waiting any device response. If available, device list will be obtained from MiniSSDPd. Default path for minissdpd socket will be used if minissdpdsock argument is NULL. If multicastif is not NULL, it will be used instead of the default multicast interface for sending SSDP discover packets. If localport is set to <a HREF="/docs/linux/man/1-upnp_local_port_same/">UPNP_LOCAL_PORT_SAME</a>(1) SSDP packets will be sent from the source port 1900 (same as destination port), if set to UPNP_LOCAL_PORT_ANY(0) system assign a source port, any other value will be attempted as the source port. If ipv6 is not 0, IPv6 is used instead of IPv4 for the discovery process.
<dt>void freeUPNPDevlist(struct UPNPDev * devlist);
<dd> free the list returned by upnpDiscover().
<dt>int UPNP_GetValidIGD(struct UPNPDev * devlist, struct UPNPUrls * urls, struct IGDdatas * data, char * lanaddr, int lanaddrlen);
<dd> browse the list of device returned by upnpDiscover(), find a live UPnP internet gateway device and fill structures passed as arguments with data used for UPNP methods invokation.
<dt>int UPNP_GetIGDFromUrl(const char * rootdescurl, struct UPNPUrls * urls, struct IGDdatas * data, char * lanaddr, int lanaddrlen);
<dd> permit to bypass the upnpDiscover() call if the xml root description URL of the UPnP IGD is known. Fill structures passed as arguments with data used for UPNP methods invokation.
<dt>void GetUPNPUrls(struct UPNPUrls *, struct IGDdatas *, const char *);
<dd>
<dt>void FreeUPNPUrls(struct UPNPUrls *);
<dd> 

</dl>

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-minissdpd/">minissdpd</a>(1)

<h2>BUGS</h2>

 

<h2>Index</h2>


