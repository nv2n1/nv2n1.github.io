---
title: "dat-conf(5)"
name: "dat-conf"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dat-conf/"
---

dat.conf - configuration file for static registration of user-level DAT rdma providers

<h2>Description</h2>

The DAT (direct access transport) architecture supports the use of multiple DAT providers within a single consumer application. Consumers implicitly select a provider using the Interface Adapter name parameter passed to dat_ia_open(). The subsystem that maps Interface Adapter names to provider implementations is known as the DAT registry. When a consumer calls dat_ia_open(), the appropriate provider is found and notified of the consumer's request to access the IA. After this point, all DAT API calls acting on DAT objects are automatically directed to the appropriate provider entry points. A persistent, administratively configurable database is used to store mappings from IA names to provider information. This provider information includes: the file system path to the provider library object, version information, and thread safety information. The location and format of the registry is platform dependent. This database is known as the Static Registry (SR) and is provided via entries in the <i>dat.conf</i> file. The process of adding a provider entry is termed Static Registration. 

<h2>Registry File Format</h2>

acters after # on a line are ignored (comments). 
&nbsp;<wbr>*&nbsp;<wbr>Lines on which there are no characters other than whitespace 
and comments are considered blank lines and are ignored. 
&nbsp;<wbr>*&nbsp;<wbr>Non-blank lines must have seven whitespace separated fields. 
These fields may contain whitespace if the field is quoted 
with double quotes. Within fields quoated with double quotes, 
the backslash or qoute are valid escape sequences: 
&nbsp;<wbr>*&nbsp;<wbr>Each non-blank line will contain the following fields: 
&nbsp;<wbr>&nbsp;<wbr>- The IA Name. 
&nbsp;<wbr>&nbsp;<wbr>- The API version of the library: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[k|u]major.minor where&nbsp;<wbr>&quot;major&quot;&nbsp;<wbr>and&nbsp;<wbr>&quot;minor&quot;&nbsp;<wbr>are both integers 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in decimal format. User-level examples:&nbsp;<wbr>&quot;u1.2&quot;, and&nbsp;<wbr>&quot;u2.0&quot;. 
&nbsp;<wbr>&nbsp;<wbr>- Whether the library is thread-safe:&nbsp;<wbr>[threadsafe|nonthreadsafe] 
&nbsp;<wbr>&nbsp;<wbr>- Whether this is the default section:&nbsp;<wbr>[default|nondefault] 
&nbsp;<wbr>&nbsp;<wbr>- The library image, version included, to be loaded. 
&nbsp;<wbr>&nbsp;<wbr>- The vendor id and version of DAPL provider: id.major.minor&nbsp;<wbr>&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>- ia params, IA specific parameters - device name and port 
&nbsp;<wbr>&nbsp;<wbr>- platform params,&nbsp;<wbr>(not used)&nbsp;<wbr>

<h2>OpenFabrics RDMA providers:</h2>

ovider options for both 1.2 and 2.0, each using different CM services 

 
&nbsp;<wbr>&nbsp;<wbr>1. cma - OpenFabrics rdma_cm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- uses rdma_cm services for connections 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- requires IPoIB and SA/SM services for IB 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- netdev used for device name, without port designation&nbsp;<wbr>(ia_params)&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- Supports any transport rdma_cm supports including IB, iWARP, RoCEE 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- libdaplcma.so&nbsp;<wbr>(1.2), libdaplofa&nbsp;<wbr>(2.0) 

 
&nbsp;<wbr>&nbsp;<wbr>2. scm - uDAPL socket based CM&nbsp;<wbr>&nbsp;<wbr>- exchanges CM information over sockets&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- eliminates the need for rdma_cm, IPoIB, and SA for IB 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- verbs device used for device name with port designation&nbsp;<wbr>(ia_param) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- Supports IB, RoCEE. Doesn't support iWARP 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- libdaplscm.so&nbsp;<wbr>(1.2), libdaploscm&nbsp;<wbr>(2.0) 

 
&nbsp;<wbr>&nbsp;<wbr>3. ucm - uDAPL unreliable IB CM - exchanges CM information via IB UD QP's 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- eliminates the need for sockets or rdma_cm 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- verbs device used for device name with port designation&nbsp;<wbr>(ia_param) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- Supports IB only, no name service.&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- libdaplucm.so&nbsp;<wbr>(1.2), libdaploucm&nbsp;<wbr>(2.0)

<h2>Example entries for each OpenFabrics provider</h2>

brics rdma_cm (v1.2 and v2.0 examples) 

 
&nbsp;<wbr>&nbsp;<wbr>OpenIB-cma u1.2 nonthreadsafe default libdaplcma.so.1 dapl.1.2&nbsp;<wbr>&quot;ib0 0&quot;&nbsp;<wbr>&quot;&quot; 
&nbsp;<wbr>&nbsp;<wbr>ofa-v2-ib0 u2.0 nonthreadsafe default libdaplofa.so.2 dapl.2.0&nbsp;<wbr>&quot;ib0 0&quot;&nbsp;<wbr>&quot;&quot; 
&nbsp;<wbr>&nbsp;<wbr>ofa-v2-iwarp u2.0 nonthreadsafe default libdaplofa.so.2 dapl.2.0&nbsp;<wbr>&quot;eth2 0&quot;&nbsp;<wbr>&quot;&quot; 
&nbsp;<wbr>&nbsp;<wbr>ofa-v2-cma-roe-eth2 u2.0 nonthreadsafe default libdaplofa.so.2 dapl.2.0&nbsp;<wbr>&quot;eth2 0&quot;&nbsp;<wbr>&quot;&quot; 
&nbsp;<wbr>&nbsp;<wbr>ofa-v2-cma-roe-eth3 u2.0 nonthreadsafe default libdaplofa.so.2 dapl.2.0&nbsp;<wbr>&quot;eth3 0&quot;&nbsp;<wbr>&quot;&quot; 

 
&nbsp;<wbr>&nbsp;<wbr>NOTE: The OpenFabrics CMA providers use&nbsp;<wbr>&lt;ia_params&gt;&nbsp;<wbr>to specify the device with one of the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>network address, network hostname, or netdev name;&nbsp;<wbr>along with port number. 

 
&nbsp;<wbr>&nbsp;<wbr>2. scm - uDAPL socket based CM&nbsp;<wbr>(v1.2 and v2.0 examples) 

 
&nbsp;<wbr>&nbsp;<wbr>OpenIB-mlx4_0-1 u1.2 nonthreadsafe default libdaplscm.so.1 dapl.1.2&nbsp;<wbr>&quot;mlx4_0 1&quot;&nbsp;<wbr>&quot;&quot; 
&nbsp;<wbr>&nbsp;<wbr>OpenIB-ipath0-1 u1.2 nonthreadsafe default libdaplscm.so.1 dapl.1.2&nbsp;<wbr>&quot;ipath0 1&quot;&nbsp;<wbr>&quot;&quot; 
&nbsp;<wbr>&nbsp;<wbr>ofa-v2-mlx4_0-1 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0&nbsp;<wbr>&quot;mlx4_0 1&quot;&nbsp;<wbr>&quot;&quot; 
&nbsp;<wbr>&nbsp;<wbr>ofa-v2-mlx4_0-2 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0&nbsp;<wbr>&quot;mlx4_0 2&quot;&nbsp;<wbr>&quot;&quot; 
&nbsp;<wbr>&nbsp;<wbr>ofa-v2-mlx4_1-1 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0&nbsp;<wbr>&quot;mlx4_1 1&quot;&nbsp;<wbr>&quot;&quot; 
&nbsp;<wbr>&nbsp;<wbr>ofa-v2-ehca0-1 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0&nbsp;<wbr>&quot;ehca0 1&quot;&nbsp;<wbr>&quot;&quot; 
&nbsp;<wbr>&nbsp;<wbr>ofa-v2-scm-roe-mlx4_0-1 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0&nbsp;<wbr>&quot;mlx4_0 1&quot;&nbsp;<wbr>&quot;&quot; 

 
&nbsp;<wbr>&nbsp;<wbr>3. ucm - uDAPL unreliable IB CM&nbsp;<wbr>&nbsp;<wbr>(not supported in 1.2, v2.0 examples) 

 
&nbsp;<wbr>&nbsp;<wbr>ofa-v2-mlx4_0-1u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0&nbsp;<wbr>&quot;mlx4_0 1&quot;&nbsp;<wbr>&quot;&quot; 
&nbsp;<wbr>&nbsp;<wbr>ofa-v2-mlx4_0-2u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0&nbsp;<wbr>&quot;mlx4_0 2&quot;&nbsp;<wbr>&quot;&quot; 
&nbsp;<wbr>&nbsp;<wbr>ofa-v2-ipath0-1u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0&nbsp;<wbr>&quot;ipath0 1&quot;&nbsp;<wbr>&quot;&quot; 
&nbsp;<wbr>&nbsp;<wbr>ofa-v2-ehca0-1u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0&nbsp;<wbr>&quot;ehca0 1&quot;&nbsp;<wbr>&quot;&quot; 

 
&nbsp;<wbr>&nbsp;<wbr>Note: OpenIB- and ofa-v2- IA names are unique mappings, reserved for OpenFabrics providers. 

 The default location for this configuration file is /etc/dat.conf. 

 The file location may be overridden with the environment variable DAT_OVERRIDE=/your_own_directory/your_dat.conf.

<h2>SEE ALSO rdma_cm verbs socket</h2>


