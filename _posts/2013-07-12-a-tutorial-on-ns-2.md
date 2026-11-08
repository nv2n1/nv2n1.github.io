---
title: "NS-2 Network Simulator: A Practical Tutorial"
date: 2013-07-12 16:32:26 +0000
modified: 2026-04-12 16:45:40 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /a-tutorial-on-ns-2/
---

ns-2 reached end-of-life in 2011 and is no longer maintained. If you’re looking to simulate network behavior, you should use **ns-3** instead, which is actively developed and provides significantly better accuracy and modern tooling.

## Why ns-3 Over ns-2

ns-2 was influential in academic networking research, but its architecture has fundamental limitations that became apparent over time. ns-3 was designed from scratch to address these:

- **Better modularity**: ns-3 uses a cleaner C++ design without the Tcl/C++ dual-language requirement that made ns-2 debugging painful
- **Active maintenance**: Regular updates, security patches, and community support
- **Improved accuracy**: Better packet-level simulation fidelity and more realistic protocol implementations
- **Modern workflow**: Better integration with version control, testing frameworks, and Python bindings
- **Extensive model library**: More complete implementations of standard protocols (TCP variants, queuing disciplines, WiFi standards)

## Getting Started with ns-3

If you’re coming from ns-2 or starting fresh with network simulation, ns-3 is the right choice. The official documentation at <a href="https://www.nsnam.org/" rel="nofollow noopener" target="_blank">https://www.nsnam.org/</a> is comprehensive and regularly updated.

### Basic ns-3 Example

Here’s a minimal topology to get you started:

``` cpp
#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"

using namespace ns3;

int main(int argc, char *argv[])
{
  // Create two nodes
  NodeContainer nodes;
  nodes.Create(2);

  // Create a point-to-point link (1Mbps, 10ms delay)
  PointToPointHelper pointToPoint;
  pointToPoint.SetDeviceAttribute("DataRate", StringValue("1Mbps"));
  pointToPoint.SetChannelAttribute("Delay", StringValue("10ms"));

  NetDeviceContainer devices;
  devices = pointToPoint.Install(nodes);

  // Install Internet stack
  InternetStackHelper stack;
  stack.Install(nodes);

  // Assign IP addresses
  Ipv4AddressHelper address;
  address.SetBase("10.1.1.0", "255.255.255.0");
  Ipv4InterfaceContainer interfaces = address.Assign(devices);

  // Create a UDP echo server on node 1
  UdpEchoServerHelper echoServer(9);
  ApplicationContainer serverApps = echoServer.Install(nodes.Get(1));
  serverApps.Start(Seconds(0.0));
  serverApps.Stop(Seconds(10.0));

  // Create a UDP echo client on node 0
  UdpEchoClientHelper echoClient(interfaces.GetAddress(1), 9);
  echoClient.SetAttribute("MaxPackets", UintegerValue(1));
  echoClient.SetAttribute("Interval", TimeValue(Seconds(1.0)));
  echoClient.SetAttribute("PacketSize", UintegerValue(1024));

  ApplicationContainer clientApps = echoClient.Install(nodes.Get(0));
  clientApps.Start(Seconds(2.0));
  clientApps.Stop(Seconds(10.0));

  Simulator::Run();
  Simulator::Destroy();

  return 0;
}
```

## If You Must Work with ns-2

If you’re maintaining legacy code or working with specific ns-2-based research, understand that:

- Bug fixes won’t be released
- Documentation is static and won’t reflect modern networking standards
- Integration with new tools is limited
- Security vulnerabilities won’t be patched
- The Tcl scripting dependency makes it difficult to maintain on newer systems

Consider a migration path to ns-3 instead of investing further in ns-2-based simulations.

## Resources for Network Simulation

- **ns-3 Tutorial & Manual**: <a href="https://www.nsnam.org/documentation/" rel="nofollow noopener" target="_blank">https://www.nsnam.org/documentation/</a>
- **ns-3 Models**: Extensive library covering 802.11, LTE, TCP variants, and more
- **Python API**: ns-3 has solid Python bindings if you prefer scripting over C++
- **Alternatives**: If ns-3 feels heavyweight, consider **Mininet** for network emulation (which runs real kernel networking code) or **OMNeT++** for event-driven simulation

For new projects, ns-3 is the standard choice in both academia and industry. The learning curve is worth the investment given the tool’s maturity and active ecosystem.
