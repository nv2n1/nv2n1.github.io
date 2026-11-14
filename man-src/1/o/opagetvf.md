---
title: "opagetvf(1)"
name: "opagetvf"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opagetvf/"
---

<h2>NAME</h2>

 opagetvf 

 

 

 Used for scripting application use of vFabrics, such as for mpirun parameters. You can query by VF Name, VF Index, Service ID, MGID, PKey, or SL. Fetches the Virtual Fabric info in a delimited format. Returns exactly one matching VF. When multiple VFs match the query, it prefers non-default VFs in which the calling server is a full member. If multiple choices remain, it returns the one with the lowest VF Index. Uses the same algorithm as the Distributed SA Plug-in (DSAP). 

 The tool can be used with additional scripts to help set PKey, SL, MTU, and Rate when running MPI jobs. Internally, this tool is based on the opasaquery -o vfinfocsv command. For more information, see <i>opasaquery</i>

<h2>Syntax</h2>

 opagetvf [-h <i>hfi</i>] [-p <i>port</i>] [-e] [-d <i>vfname</i>|-S <i>serviceId</i>|-m <i>mcgid</i>|-i <i>vfIndex</i>| -k <i>pkey</i>|-L <i>sl</i>]

<h2>Options</h2>

 

<dl>
<dt>--help
<dd> Produces full help text.
<dt>-h <i>hfi</i>
<dd> HFI to send by. Default is first HFI.
<dt>-p <i>port</i>
<dd> Port to send by, default is first active port.
<dt>-e
<dd> Output MTU and rate as enum values.
<dt>-d <i>vfname</i>
<dd> Queries by VirtualFabric Name.
<dt>-S <i>serviceId</i>
<dd> Queries by Application ServiceId.
<dt>-m <i>gid</i>
<dd> Queries by Application Multicast GID.
<dt>-i <i>vfindex</i>
<dd> Queries by VirtualFabric Index.
<dt>-k <i>pkey</i>
<dd> Queries by VirtualFabric PKey.
<dt>-L <i>SL</i>
<dd> Queries by VirtualFabric SL.</dl>

<h2>Examples</h2>

 opagetvf -d 'Compute' 
 opagetvf -h 2 -p 2 -d 'Compute'

<h2>Sample Outputs</h2>

 

 

 The output is of the form: name:index:pkey:sl:mtu:rate:optionflag as shown in the following example. 

 Option flag (bitmask) values include:
<dl>
<dt>&bull;
<dd> 0x00 Indicates no bits are set. Specifically, no QOS, no Security, and no flow control disabled (which means flow control is enabled).
<dt>&bull;
<dd> 0x01 Security
<dt>&bull;
<dd> 0x02 QOS
<dt>&bull;
<dd> 0x04 Flow Control Disable</dl>
 

 

 
 # opagetvf -d Default 
 Default:0:0xffff:0:unlimited:unlimited:0x0 

 
 

<h2>Index</h2>


