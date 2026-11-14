---
title: "globus_xio_data_descriptors(3)"
name: "globus_xio_data_descriptors"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_data_descriptors/"
---

<h2 class="name">NAME</h2>
 

 Data descriptors - globus_xio uses data descriptors to associate meta data with the data being written or the data read. 

 Data descriptors flow into the drivers read and write interface functions by way of the operation structure. If the driver is interested in viewing the data descriptor it can request it from the operation structure via a call to globus_xio_driver_operation_get_data_descriptor() and it can view any driver specific data descriptor via a call to globus_xio_driver_data_descriptor_get_specific(). The driver can modify values in the data descriptor by setting values before passing the request down the stack. Several functions are available to modify the data descriptors. There is no need to 'set()' the data descriptors back into the operation. The functions for manipulating the values in a DD affect the values xio has directly. 

 Data descriptors flow back to the driver in the callbacks for the data operations. When calling finished operation on a data operation the driver must pass in a data descriptor. It should get this data descriptor from the io operation callback. 

 Life Cycle: 

 Passing in a data descriptor: A data descriptor is first created by the globus_xio user. The user can add driver specific data descriptors to it. Once the user has created and set the attributes on its data descriptor to their liking they pass it into a globus_xio data operation (either read or write). When the data descriptor is passed on globus_xio will make an internal copy of it. It does this by first coping the user the level data descriptor and then walking through the list of driver specific data descriptor contained in to and requesting the driver make a copy of the driver specific data descriptor. If ever a driver specific data descriptor is NULL globus_xio need not call into its drivers dd_copy function. If ever the user level data descriptor is NULL globus_xio need not deal with the data descriptor functionality at all. 

 A data descriptor coming back up the stack Once an io operation reaches the transport driver (the bottom of the stack) it takes on a slightly different role. On the way in it is describing what is requested to be done with the data, on the way out it is describing what has actually been done. Once the transport driver performs the operation it should adjust the data descriptor to reflect what has actually happened (few drivers will need to worry about this). Each driver on the way up can adjust the data descriptor and its driver specific data descriptor. When XIO reaches the top of the stack it calls a user callback. When that callback returns all memory associated with the data descriptor is cleaned up. The interface function globus_xio_driver_data_descriptor_free() is used for this. 

<h2>Author</h2>

 

 Generated automatically by Doxygen for globus_xio from the source code. 

<h2>Index</h2>


