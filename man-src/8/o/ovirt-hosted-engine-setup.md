---
title: "ovirt-hosted-engine-setup(8)"
name: "ovirt-hosted-engine-setup"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovirt-hosted-engine-setup/"
description: "ovirt-hosted-engine-setup – Tool for deploying hosted engine VM"
---

<p>ovirt-hosted-engine-setup &#8211; Tool for deploying hosted engine VM</p>
<h2>Synopsis</h2>
<p><code>ovirt-hosted-engine-setup</code> [options] </p>
<h2>Description</h2>
<p>The <code>ovirt-hosted-engine-setup</code> command deploys a virtual machine that you can install oVirt Open Virtualization Manager on to. The Manager installation on your hosted-engine virtual machine can manage the host it is running on. </p>
<h2>Options</h2>
<p>The following are general options you can use with this command:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Show the help message and exit.</p>
<dt><code>&#8211;config-append=file</code></p>
<dd>Load extra configuration files. The format of the files is the same used in generated answer files.</p>
<dt><code>&#8211;generate-answer=file</code></p>
<dd>Generate answer file to the specified path instead of using the default location: /etc/ovirt-hosted-engine/answers.conf</p>
<dt><code>&#8211;upgrade-appliance</code></p>
<dd>Upgrade the engine appliance.</p>
<dt><code>&#8211;rollback-upgrade</code></p>
<dd>Rollback using a backup saved in a previous upgrade attempt. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/ovirt-hosted-engine/answers.conf</i></p>
<dd>Default location for generated answer file. The file must be used on additional hosts using the option &#8211;config-append </p>
</dl>
<h2>Example</h2>
<p>This is an answers.conf example file: </p>
<pre>[environment:default]
OVEHOSTED_NETWORK/bridgeIf=none:None
OVEHOSTED_NETWORK/fqdn=str:ovirt.home
OVEHOSTED_NETWORK/bridgeName=str:ovirtmgmt
OVEHOSTED_NETWORK/firewallManager=str:firewalld
OVEHOSTED_NETWORK/gateway=str:192.168.1.1
OVEHOSTED_STORAGE/storageDatacenterName=str:hosted_datacenter
OVEHOSTED_STORAGE/storageDomainName=str:hosted_storage
OVEHOSTED_STORAGE/hostID=int:1
OVEHOSTED_STORAGE/storageType=none:None
OVEHOSTED_STORAGE/volUUID=str:272b4067-1ae4-4755-b2e3-96bb600006e7
OVEHOSTED_STORAGE/domainType=str:nfs3
OVEHOSTED_STORAGE/imgSizeGB=str:25
OVEHOSTED_STORAGE/storageDomainConnection=str:server.home:/home/images
OVEHOSTED_STORAGE/connectionUUID=str:ca50f16a-23ab-465c-914b-b132f07a7151
OVEHOSTED_STORAGE/spUUID=str:8018650a-4c64-48fb-a98e-5602bba3086e
OVEHOSTED_STORAGE/imgUUID=str:c7d69e7a-d934-423c-93d6-ca45c5882806
OVEHOSTED_STORAGE/sdUUID=str:1d6f6bca-467e-4890-b220-dd2d9b204ab5
OVEHOSTED_VM/vmVCpus=str:2
OVEHOSTED_VDSM/consoleType=str:vnc
OVEHOSTED_VM/vmBoot=str:pxe
OVEHOSTED_VM/vmMemSizeMB=str:4096
OVEHOSTED_VM/vmUUID=str:ab35151c-7661-475e-aeaf-adc6fb45e399
OVEHOSTED_VM/vmMACAddr=str:00:16:3e:1b:d7:61
OVEHOSTED_VM/vmCDRom=none:None
OVEHOSTED_VM/ovfArchive=none:None
OVEHOSTED_VDSM/spicePkiSubject=str:O=home, CN=server.home
OVEHOSTED_VDSM/pkiSubject=str:/C=EN/L=Test/O=Test/CN=Test</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-hosted-engine/">hosted-engine</a></code>(8) </p>
