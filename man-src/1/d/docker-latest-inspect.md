---
title: "docker-latest-inspect(1)"
name: "docker-latest-inspect"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-inspect/"
description: "docker-inspect – Return low-level information on a container or image"
---

<h2 class="name">NAME</h2>
<p> docker-inspect &#8211; Return low-level information on a container or image </p>
<h2>SYNOPSIS</h2>
<p> <code>docker inspect</code> [<code>&#8211;help</code>] [<code>-f</code>|<code>&#8211;format</code>[=<i>FORMAT</i>]] [<code>-s</code>|<code>&#8211;size</code>] [<code>&#8211;type</code>=<i>container</i>|<i>image</i>] CONTAINER|IMAGE [CONTAINER|IMAGE&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> This displays all the information available in Docker for a given container or image. By default, this will render all results in a JSON array. If the container and image have the same name, this will return container JSON for unspecified type. If a format is specified, the given template will be executed for each result. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>Print usage statement </p>
<p> <code>-f</code>, <code>&#8211;format</code>=&quot;&quot;<br />
&nbsp;<wbr>Format the output using the given Go template. </p>
<p> <code>-s</code>, <code>&#8211;size</code><br />
&nbsp;<wbr>Display total file sizes if the type is container. </p>
<p> <code>&#8211;type</code>=&quot;<i>container</i>|<i>image</i>&quot;<br />
&nbsp;<wbr>Return JSON for specified type, permissible values are&nbsp;<wbr>&quot;image&quot;&nbsp;<wbr>or&nbsp;<wbr>&quot;container&quot; </p>
<h2>EXAMPLES</h2>
<p> Get information about an image when image name conflicts with the container name, e.g. both image and container are named rhel7: </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker inspect-- type = image rhel7
    [{
        "Id" : "fe01a428b9d9de35d29531e9994157978e8c48fa693e1bf1d221dffbbb67b170",
        "Parent" : "10acc31def5d6f249b548e01e8ffbaccfd61af0240c17315a7ad393d022c5ca2",
        ....
    }]
</code></pre>
</dl>
<h2>Getting information on a container</h2>
<p> To get information on a container use its ID or instance name: </p>
<dl>
<dt>
<dd>
<p>$ docker inspect d2cc496561d6<br />
    [{<br />
        &#8220;Id&#8221; : &#8220;d2cc496561d6d520cbc0236b4ba88c362c446a7619992123f11c809cded25b47&#8221;,<br />
        &#8220;Created&#8221; : &#8220;2015-06-08T16:18:02.505155285Z&#8221;,<br />
        &#8220;Path&#8221; : &#8220;bash&#8221;,<br />
        &#8220;Args&#8221; : [],<br />
        &#8220;State&#8221; : {<br />
            &#8220;Running&#8221; : false,<br />
            &#8220;Paused&#8221; : false,<br />
            &#8220;Restarting&#8221; : false,<br />
            &#8220;OOMKilled&#8221; : false,<br />
            &#8220;Dead&#8221; : false,<br />
            &#8220;Pid&#8221; : 0,<br />
            &#8220;ExitCode&#8221; : 0,<br />
            &#8220;Error&#8221; : &#8220;&#8221;,<br />
            &#8220;StartedAt&#8221; : &#8220;2015-06-08T16:18:03.643865954Z&#8221;,<br />
            &#8220;FinishedAt&#8221; : &#8220;2015-06-08T16:57:06.448552862Z&#8221;<br />
        },<br />
        &#8220;Image&#8221; : &#8220;ded7cd95e059788f2586a51c275a4f151653779d6a7f4dad77c2bd34601d94e4&#8221;,<br />
        &#8220;NetworkSettings&#8221; : {<br />
            &#8220;Bridge&#8221; : &#8220;&#8221;,<br />
            &#8220;SandboxID&#8221; : &#8220;6b4851d1903e16dd6a567bd526553a86664361f31036eaaa2f8454d6f4611f6f&#8221;,<br />
            &#8220;HairpinMode&#8221; : false,<br />
            &#8220;LinkLocalIPv6Address&#8221; : &#8220;&#8221;,<br />
            &#8220;LinkLocalIPv6PrefixLen&#8221; : 0,<br />
            &#8220;Ports&#8221; : {},<br />
            &#8220;SandboxKey&#8221; : &#8220;/var/run/docker/netns/6b4851d1903e&#8221;,<br />
            &#8220;SecondaryIPAddresses&#8221; : null,<br />
            &#8220;SecondaryIPv6Addresses&#8221; : null,<br />
            &#8220;EndpointID&#8221; : &#8220;7587b82f0dada3656fda26588aee72630c6fab1536d36e394b2bfbcf898c971d&#8221;,<br />
            &#8220;Gateway&#8221; : &#8220;172.17.0.1&#8221;,<br />
            &#8220;GlobalIPv6Address&#8221; : &#8220;&#8221;,<br />
            &#8220;GlobalIPv6PrefixLen&#8221; : 0,<br />
            &#8220;IPAddress&#8221; : &#8220;172.17.0.2&#8221;,<br />
            &#8220;IPPrefixLen&#8221; : 16,<br />
            &#8220;IPv6Gateway&#8221; : &#8220;&#8221;,<br />
            &#8220;MacAddress&#8221; : &#8220;02:42:ac:12:00:02&#8221;,<br />
            &#8220;Networks&#8221; : {<br />
                &#8220;bridge&#8221; : {<br />
                    &#8220;NetworkID&#8221; : &#8220;7ea29fc1412292a2d7bba362f9253545fecdfa8ce9a6e37dd10ba8bee7129812&#8221;,<br />
                    &#8220;EndpointID&#8221; : &#8220;7587b82f0dada3656fda26588aee72630c6fab1536d36e394b2bfbcf898c971d&#8221;,<br />
                    &#8220;Gateway&#8221; : &#8220;172.17.0.1&#8221;,<br />
                    &#8220;IPAddress&#8221; : &#8220;172.17.0.2&#8221;,<br />
                    &#8220;IPPrefixLen&#8221; : 16,<br />
                    &#8220;IPv6Gateway&#8221; : &#8220;&#8221;,<br />
                    &#8220;GlobalIPv6Address&#8221; : &#8220;&#8221;,<br />
                    &#8220;GlobalIPv6PrefixLen&#8221; : 0,<br />
                    &#8220;MacAddress&#8221; : &#8220;02:42:ac:12:00:02&#8221;<br />
                }<br />
            }<br />
        },<br />
        &#8220;ResolvConfPath&#8221; : &#8220;/var/lib/docker/containers/d2cc496561d6d520cbc0236b4ba88c362c446a7619992123f11c809cded25b47/resolv.conf&#8221;,<br />
        &#8220;HostnamePath&#8221; : &#8220;/var/lib/docker/containers/d2cc496561d6d520cbc0236b4ba88c362c446a7619992123f11c809cded25b47/hostname&#8221;,<br />
        &#8220;HostsPath&#8221; : &#8220;/var/lib/docker/containers/d2cc496561d6d520cbc0236b4ba88c362c446a7619992123f11c809cded25b47/hosts&#8221;,<br />
        &#8220;LogPath&#8221; : &#8220;/var/lib/docker/containers/d2cc496561d6d520cbc0236b4ba88c362c446a7619992123f11c809cded25b47/d2cc496561d6d520cbc0236b4ba88c362c446a7619992123f11c809cded25b47-json.log&#8221;,<br />
        &#8220;Name&#8221; : &#8220;/adoring_wozniak&#8221;,<br />
        &#8220;RestartCount&#8221; : 0,<br />
        &#8220;Driver&#8221; : &#8220;devicemapper&#8221;,<br />
        &#8220;MountLabel&#8221; : &#8220;&#8221;,<br />
        &#8220;ProcessLabel&#8221; : &#8220;&#8221;,<br />
        &#8220;Mounts&#8221; : [<br />
            {<br />
                &#8220;Source&#8221; : &#8220;/data&#8221;,<br />
                &#8220;Destination&#8221; : &#8220;/data&#8221;,<br />
                &#8220;Mode&#8221; : &#8220;ro,Z&#8221;,<br />
                &#8220;RW&#8221; : false &#8220;Propagation&#8221; : &#8220;&#8221;<br />
            }<br />
        ],<br />
        &#8220;AppArmorProfile&#8221; : &#8220;&#8221;,<br />
        &#8220;ExecIDs&#8221; : null,<br />
        &#8220;HostConfig&#8221; : {<br />
            &#8220;Binds&#8221; : null,<br />
            &#8220;ContainerIDFile&#8221; : &#8220;&#8221;,<br />
            &#8220;Memory&#8221; : 0,<br />
            &#8220;MemorySwap&#8221; : 0,<br />
            &#8220;CpuShares&#8221; : 0,<br />
            &#8220;CpuPeriod&#8221; : 0,<br />
            &#8220;CpusetCpus&#8221; : &#8220;&#8221;,<br />
            &#8220;CpusetMems&#8221; : &#8220;&#8221;,<br />
            &#8220;CpuQuota&#8221; : 0,<br />
            &#8220;BlkioWeight&#8221; : 0,<br />
            &#8220;OomKillDisable&#8221; : false,<br />
            &#8220;Privileged&#8221; : false,<br />
            &#8220;PortBindings&#8221; : {},<br />
            &#8220;Links&#8221; : null,<br />
            &#8220;PublishAllPorts&#8221; : false,<br />
            &#8220;Dns&#8221; : null,<br />
            &#8220;DnsSearch&#8221; : null,<br />
            &#8220;DnsOptions&#8221; : null,<br />
            &#8220;ExtraHosts&#8221; : null,<br />
            &#8220;VolumesFrom&#8221; : null,<br />
            &#8220;Devices&#8221; : [],<br />
            &#8220;NetworkMode&#8221; : &#8220;bridge&#8221;,<br />
            &#8220;IpcMode&#8221; : &#8220;&#8221;,<br />
            &#8220;PidMode&#8221; : &#8220;&#8221;,<br />
            &#8220;UTSMode&#8221; : &#8220;&#8221;,<br />
            &#8220;CapAdd&#8221; : null,<br />
            &#8220;CapDrop&#8221; : null,<br />
            &#8220;RestartPolicy&#8221; : {<br />
                &#8220;Name&#8221; : &#8220;no&#8221;,<br />
                &#8220;MaximumRetryCount&#8221; : 0<br />
            },<br />
            &#8220;SecurityOpt&#8221; : null,<br />
            &#8220;ReadonlyRootfs&#8221; : false,<br />
            &#8220;Ulimits&#8221; : null,<br />
            &#8220;LogConfig&#8221; : {<br />
                &#8220;Type&#8221; : &#8220;json-file&#8221;,<br />
                &#8220;Config&#8221; : {}<br />
            },<br />
            &#8220;CgroupParent&#8221; : &#8220;&#8221;<br />
        },<br />
        &#8220;GraphDriver&#8221; : {<br />
            &#8220;Name&#8221; : &#8220;devicemapper&#8221;,<br />
            &#8220;Data&#8221; : {<br />
                &#8220;DeviceId&#8221; : &#8220;5&#8221;,<br />
                &#8220;DeviceName&#8221; : &#8220;docker-253:1-2763198-d2cc496561d6d520cbc0236b4ba88c362c446a7619992123f11c809cded25b47&#8221;,<br />
                &#8220;DeviceSize&#8221; : &#8220;171798691840&#8221;<br />
            }<br />
        },<br />
        &#8220;Config&#8221; : {<br />
            &#8220;Hostname&#8221; : &#8220;d2cc496561d6&#8221;,<br />
            &#8220;Domainname&#8221; : &#8220;&#8221;,<br />
            &#8220;User&#8221; : &#8220;&#8221;,<br />
            &#8220;AttachStdin&#8221; : true,<br />
            &#8220;AttachStdout&#8221; : true,<br />
            &#8220;AttachStderr&#8221; : true,<br />
            &#8220;ExposedPorts&#8221; : null,<br />
            &#8220;Tty&#8221; : true,<br />
            &#8220;OpenStdin&#8221; : true,<br />
            &#8220;StdinOnce&#8221; : true,<br />
            &#8220;Env&#8221; : null,<br />
            &#8220;Cmd&#8221; : [&#8220;bash&#8221;],<br />
            &#8220;Image&#8221; : &#8220;fedora&#8221;,<br />
            &#8220;Volumes&#8221; : null,<br />
            &#8220;VolumeDriver&#8221; : &#8220;&#8221;,<br />
            &#8220;WorkingDir&#8221; : &#8220;&#8221;,<br />
            &#8220;Entrypoint&#8221; : null,<br />
            &#8220;NetworkDisabled&#8221; : false,<br />
            &#8220;MacAddress&#8221; : &#8220;&#8221;,<br />
            &#8220;OnBuild&#8221; : null,<br />
            &#8220;Labels&#8221; : {},<br />
            &#8220;Memory&#8221; : 0,<br />
            &#8220;MemorySwap&#8221; : 0,<br />
            &#8220;CpuShares&#8221; : 0,<br />
            &#8220;Cpuset&#8221; : &#8220;&#8221;,<br />
            &#8220;StopSignal&#8221; : &#8220;SIGTERM&#8221;<br />
        }<br />
    }]
</dl>
<h2>Getting the IP address of a container instance</h2>
<p> To get the IP address of a container use: </p>
<dl>
<dt>
<dd>
<p>$ docker inspect&#8211; format = &#8216;&#123;&#123;range .NetworkSettings.Networks}}&#123;&#123;.IPAddress}}&#123;&#123;end}}&#8217; d2cc496561d6 172.17.0.2
</dl>
<h2>Listing all port bindings</h2>
<p> One can loop over arrays and maps in the results to produce simple text output: </p>
<dl>
<dt>
<dd>
<p>$ docker inspect&#8211; format = &#8216;&#123;&#123;range $p, $conf := .NetworkSettings.Ports}} \<br />
  &#123;&#123;$p}} -&gt; &#123;&#123;(index $conf 0).HostPort}} &#123;&#123;end}}&#8217; d2cc496561d6 80 /<br />
                            tcp-&gt;80
</dl>
<p> You can get more information about how to write a Go template from: </p>
<p> &lt;<a rel="nofollow" href="https://golang.org/pkg/text/template/">https://golang.org/pkg/text/template/</a>&gt;. </p>
<h2>Getting size information on a container</h2>
<dl>
<dt>
<dd>
<p>$ docker inspect &#8211; s d2cc496561d6<br />
                       [{<br />
                           &#8220;SizeRw&#8221; : 0,<br />
                           &#8220;SizeRootFs&#8221; : 972,<br />
                       }]
</dl>
<h2>Getting information on an image</h2>
<p> Use an image&#8217;s ID or name (e.g., repository/name[:tag]) to get information about the image: </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker inspect ded7cd95e059
    [{
        "Id" : "ded7cd95e059788f2586a51c275a4f151653779d6a7f4dad77c2bd34601d94e4",
        "Parent" : "48ecf305d2cf7046c1f5f8fcbcd4994403173441d4a7f125b1bb0ceead9de731",
        "Comment" : "",
        "Created" : "2015-05-27T16:58:22.937503085Z",
        "Container" : "76cf7f67d83a7a047454b33007d03e32a8f474ad332c3a03c94537edd22b312b",
        "ContainerConfig" : {
            "Hostname" : "76cf7f67d83a",
            "Domainname" : "",
            "User" : "",
            "AttachStdin" : false,
            "AttachStdout" : false,
            "AttachStderr" : false,
            "ExposedPorts" : null,
            "Tty" : false,
            "OpenStdin" : false,
            "StdinOnce" : false,
            "Env" : null,
            "Cmd" : [
                "/bin/sh",
                "-c",
                "#(nop) ADD file:4be46382bcf2b095fcb9fe8334206b584eff60bb3fad8178cbd97697fcb2ea83 in /"
            ],
            "Image" : "48ecf305d2cf7046c1f5f8fcbcd4994403173441d4a7f125b1bb0ceead9de731",
            "Volumes" : null,
            "VolumeDriver" : "",
            "WorkingDir" : "",
            "Entrypoint" : null,
            "NetworkDisabled" : false,
            "MacAddress" : "",
            "OnBuild" : null,
            "Labels" : {}
        },
        "DockerVersion" : "1.6.0",
        "Author" : "Lokesh Mandvekar <lsm5 [at] fedoraproject.org>",
        "Config" : {
            "Hostname" : "76cf7f67d83a",
            "Domainname" : "",
            "User" : "",
            "AttachStdin" : false,
            "AttachStdout" : false,
            "AttachStderr" : false,
            "ExposedPorts" : null,
            "Tty" : false,
            "OpenStdin" : false,
            "StdinOnce" : false,
            "Env" : null,
            "Cmd" : null,
            "Image" : "48ecf305d2cf7046c1f5f8fcbcd4994403173441d4a7f125b1bb0ceead9de731",
            "Volumes" : null,
            "VolumeDriver" : "",
            "WorkingDir" : "",
            "Entrypoint" : null,
            "NetworkDisabled" : false,
            "MacAddress" : "",
            "OnBuild" : null,
            "Labels" : {}
        },
        "Architecture" : "amd64",
        "Os" : "linux",
        "Size" : 186507296,
        "VirtualSize" : 186507296,
        "GraphDriver" : {
            "Name" : "devicemapper",
            "Data" : {
                "DeviceId" : "3",
                "DeviceName" : "docker-253:1-2763198-ded7cd95e059788f2586a51c275a4f151653779d6a7f4dad77c2bd34601d94e4",
                "DeviceSize" : "171798691840"
            }
        }
    }]
</code></pre>
</dl>
<h2>HISTORY</h2>
<p> April 2014, originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; April 2015, updated by Qiang Huang &lt;h.huangqiang [at] huawei.com&gt; October 2015, updated by Sally O&#8217;Malley &lt;somalley [at] redhat.com&gt; </p>
<h2>Index</h2>
