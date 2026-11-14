---
title: "docker-network-inspect(1)"
name: "docker-network-inspect"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-network-inspect/"
description: "docker-network-inspect – Display detailed information on one or more networks"
---

<h2 class="name">NAME</h2>
<p> docker-network-inspect &#8211; Display detailed information on one or more networks </p>
<h2>SYNOPSIS</h2>
<p> <code>docker network inspect [OPTIONS] NETWORK [NETWORK&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> Returns information about one or more networks. By default, this command renders all results in a JSON object. For example, if you connect two containers to the default bridge network: </p>
<dl>
<dt>
<dd>
<pre>
$ sudo docker run -itd --name=container1 busybox
f2870c98fd504370fb86e59f32cd0753b1ac9b69b7d80566ffc7192a82b3ed27
$ sudo docker run -itd --name=container2 busybox
bda12f8922785d1f160be70736f26c1e331ab8aaf8ed8d56728508f2e2fd4727
</pre>
</dl>
<p> The network inspect command shows the containers, by id, in its results. You can specify an alternate format to execute a given template for each result. Go&#8217;s text/template &lt;<a rel="nofollow" href="http://golang.org/pkg/text/template/">http://golang.org/pkg/text/template/</a>&gt; package describes all the details of the format. </p>
<dl>
<dt>
<dd>
<pre><code>
$ sudo docker network inspect bridge
    [{
        "Name" : "bridge",
        "Id" : "b2b1a2cba717161d984383fd68218cf70bbbd17d328496885f7c921333228b0f",
        "Scope" : "local",
        "Driver" : "bridge",
        "IPAM" : {
            "Driver" : "default",
            "Config" : [
                {
                    "Subnet" : "172.17.42.1/16",
                    "Gateway" : "172.17.42.1"
                }
            ]
        },
        "Internal" : false,
        "Ingress" : false,
        "Containers" : {
            "bda12f8922785d1f160be70736f26c1e331ab8aaf8ed8d56728508f2e2fd4727" : {
                "Name" : "container2",
                "EndpointID" : "0aebb8fcd2b282abe1365979536f21ee4ceaf3ed56177c628eae9f706e00e019",
                "MacAddress" : "02:42:ac:11:00:02",
                "IPv4Address" : "172.17.0.2/16",
                "IPv6Address" : ""
            },
            "f2870c98fd504370fb86e59f32cd0753b1ac9b69b7d80566ffc7192a82b3ed27" : {
                "Name" : "container1",
                "EndpointID" : "a00676d9c91a96bbe5bcfb34f705387a33d7cc365bac1a29e4e9728df92d10ad",
                "MacAddress" : "02:42:ac:11:00:01",
                "IPv4Address" : "172.17.0.1/16",
                "IPv6Address" : ""
            }
        },
        "Options" : {
            "com.docker.network.bridge.default_bridge" : "true",
            "com.docker.network.bridge.enable_icc" : "true",
            "com.docker.network.bridge.enable_ip_masquerade" : "true",
            "com.docker.network.bridge.host_binding_ipv4" : "0.0.0.0",
            "com.docker.network.bridge.name" : "docker0",
            "com.docker.network.driver.mtu" : "1500"
        }
    }]
</code></pre>
</dl>
<p> Returns the information about the user-defined network: </p>
<dl>
<dt>
<dd>
<p>$ docker network create simple &#8211; network 69568e6336d8c96bbf57869030919f7c69524f71183b44d80948bd3927c87f6a $ docker network inspect simple &#8211; network[{<br />
    &#8220;Name&#8221; : &#8220;simple-network&#8221;,<br />
    &#8220;Id&#8221; : &#8220;69568e6336d8c96bbf57869030919f7c69524f71183b44d80948bd3927c87f6a&#8221;,<br />
    &#8220;Scope&#8221; : &#8220;local&#8221;,<br />
    &#8220;Driver&#8221; : &#8220;bridge&#8221;,<br />
    &#8220;IPAM&#8221; : {<br />
        &#8220;Driver&#8221; : &#8220;default&#8221;,<br />
        &#8220;Config&#8221; : [<br />
            {<br />
                &#8220;Subnet&#8221; : &#8220;172.22.0.0/16&#8221;,<br />
                &#8220;Gateway&#8221; : &#8220;172.22.0.1&#8221;<br />
            }<br />
        ]<br />
    },<br />
    &#8220;Containers&#8221; : {},<br />
    &#8220;Options&#8221; : {}<br />
}]
</dl>
<p> docker network inspect &#8211;verbose for swarm mode overlay networks shows service-specific details such as the service&#8217;s VIP and port mappings. It also shows IPs of service tasks, and the IPs of the nodes where the tasks are running. </p>
<p> Following is an example output for an overlay network ov1 that has one service s1 attached to. service s1 in this case has three replicas. </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker network inspect-- verbose ov1
    [{
        "Name" : "ov1",
        "Id" : "ybmyjvao9vtzy3oorxbssj13b",
        "Created" : "2017-03-13T17:04:39.776106792Z",
        "Scope" : "swarm",
        "Driver" : "overlay",
        "EnableIPv6" : false,
        "IPAM" : {
            "Driver" : "default",
            "Options" : null,
            "Config" : [
                {
                    "Subnet" : "10.0.0.0/24",
                    "Gateway" : "10.0.0.1"
                }
            ]
        },
        "Internal" : false,
        "Attachable" : false,
        "Ingress" : false,
        "Containers" : {
            "020403bd88a15f60747fd25d1ad5fa1272eb740e8a97fc547d8ad07b2f721c5e" : {
                "Name" : "s1.1.pjn2ik0sfgkfzed3h0s00gs9o",
                "EndpointID" : "ad16946f416562d658f3bb30b9830d73ad91ccf6feae44411269cd0ff674714e",
                "MacAddress" : "02:42:0a:00:00:04",
                "IPv4Address" : "10.0.0.4/24",
                "IPv6Address" : ""
            }
        },
        "Options" : {
            "com.docker.network.driver.overlay.vxlanid_list" : "4097"
        },
        "Labels" : {},
        "Peers" : [
            {
                "Name" : "net-3-5d3cfd30a58c",
                "IP" : "192.168.33.13"
            },
            {
                "Name" : "net-1-6ecbc0040a73",
                "IP" : "192.168.33.11"
            },
            {
                "Name" : "net-2-fb80208efd75",
                "IP" : "192.168.33.12"
            }
        ],
        "Services" : {
            "s1" : {
                "VIP" : "10.0.0.2",
                "Ports" : [],
                "LocalLBIndex" : 257,
                "Tasks" : [
                    {
                        "Name" : "s1.2.q4hcq2aiiml25ubtrtg4q1txt",
                        "EndpointID" : "040879b027e55fb658e8b60ae3b87c6cdac7d291e86a190a3b5ac6567b26511a",
                        "EndpointIP" : "10.0.0.5",
                        "Info" : {
                            "Host IP" : "192.168.33.11"
                        }
                    },
                    {
                        "Name" : "s1.3.yawl4cgkp7imkfx469kn9j6lm",
                        "EndpointID" : "106edff9f120efe44068b834e1cddb5b39dd4a3af70211378b2f7a9e562bbad8",
                        "EndpointIP" : "10.0.0.3",
                        "Info" : {
                            "Host IP" : "192.168.33.12"
                        }
                    },
                    {
                        "Name" : "s1.1.pjn2ik0sfgkfzed3h0s00gs9o",
                        "EndpointID" : "ad16946f416562d658f3bb30b9830d73ad91ccf6feae44411269cd0ff674714e",
                        "EndpointIP" : "10.0.0.4",
                        "Info" : {
                            "Host IP" : "192.168.33.13"
                        }
                    }
                ]
            }
        }
    }]
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;format</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Format the output using the given Go template</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for inspect</p>
<p> <code>-v</code>, <code>&#8211;verbose</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Verbose output for diagnostics</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-network/">docker-network</a>(1)</code> </p>
<h2>Index</h2>
