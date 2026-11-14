---
title: "pythonivi(1)"
name: "pythonivi"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pythonivi/"
description: "pythonivi – Python IVI Documentation"
---

<h2>NAME</h2>
<p> pythonivi &#8211; Python IVI Documentation </p>
<p> Python IVI is a Python-based interpretation of the Interchangeable Virtual Instrument standard from the <i>IVI foundation</i>. </p>
<p> See also:</p>
<dl>
<dt>&bull;</p>
<dd> <i>Python IVI home page</i></p>
<dt>&bull;</p>
<dd> <i>GitHub repository</i></p>
<dt>&bull;</p>
<dd> <i>IVI Foundation</i> </p>
<p> Contents:</dl>
<h2>INTRODUCTION TO PYTHON IVI</h2>
<h3>Overview</h3>
<p> Python IVI is a Python-based interpretation of the Interchangeable Virtual Instrument standard from the <i>IVI foundation</i>. The implementation is pure Python and highly portable. </p>
<p> It is released under the MIT license, see <i>LICENSE</i> for more details. </p>
<p> Copyright (C) 2012-2014 Alex Forencich &lt;<i>alex [at] alexforencich.com</i>&gt; </p>
<p> See also:</p>
<dl>
<dt>&bull;</p>
<dd> <i>Python IVI home page</i></p>
<dt>&bull;</p>
<dd> <i>GitHub repository</i></p>
<dt>&bull;</p>
<dd> <i>IVI Foundation</i></dl>
<h3>Features</h3>
<dl>
<dt>&bull;</p>
<dd> Supports Python 2 and Python 3</p>
<dt>&bull;</p>
<dd> Pure Python</p>
<dt>&bull;</p>
<dd> Highly portable</p>
<dt>&bull;</p>
<dd> Communicates with instruments with various add-on modules</dl>
<h3>Requirements</h3>
<dl>
<dt>&bull;</p>
<dd> Python 2 or Python 3</p>
<dt>&bull;</p>
<dd> One or more communication extensions</dl>
<h3>Installation</h3>
<p> To install the module for all users on the system, administrator rights (root) are required.</p>
<h3>From source</h3>
<p> Download the archive, extract, and run: </p>
<pre>
python setup.py install
</pre>
<h3>Packages</h3>
<p> There are also packaged versions for some Linux distributions:</p>
<dl>
<dt><code>Arch Linux</code></p>
<dd> Python IVI is available under the name &quot;python-ivi-git&quot; in the AUR.</dl>
<h3>Instrument Communication Extensions</h3>
<p> Python IVI does not contain any IO drivers itself. In order to communicate with an instrument, you must install one or more of the following drivers:</p>
<h3>Python VXI11</h3>
<p> Python VXI11 provides a pure python TCP/IP driver for LAN based instruments that support the VXI11 protocol. This includes most LXI instruments and also devices like the Agilent E2050 GPIB to LAN converter. </p>
<p> Home page: <i><a rel="nofollow" href="http://www.alexforencich.com/wiki/en/python-vxi11/start">http://www.alexforencich.com/wiki/en/python-vxi11/start</a></i> </p>
<p> GitHub repository: <i><a rel="nofollow" href="https://github.com/alexforencich/python-vxi11">https://github.com/alexforencich/python-vxi11</a></i></p>
<h3>Python USBTMC</h3>
<p> Python USBTMC provides a pure python USBTMC driver for instruments that support the USB Test and Measurement Class. Python USBTMC uses PyUSB to connect to the instrument in a platform-independent manner. </p>
<p> Home page: <i><a rel="nofollow" href="http://alexforencich.com/wiki/en/python-usbtmc/start">http://alexforencich.com/wiki/en/python-usbtmc/start</a></i> </p>
<p> GitHub repository: <i><a rel="nofollow" href="https://github.com/alexforencich/python-usbtmc">https://github.com/alexforencich/python-usbtmc</a></i></p>
<h3>Linux GPIB</h3>
<p> Python IVI provides an interface wrapper for the Linux GPIB driver. If the Linux GPIB driver and its included Python interface available, Python IVI can use it to communicate with instruments via any GPIB interface supported by Linux GPIB. </p>
<p> Home page: <i><a rel="nofollow" href="http://linux-gpib.sourceforge.net/">http://linux-gpib.sourceforge.net/</a></i></p>
<h3>pySerial</h3>
<p> Python IVI provides an interface wrapper for the pySerial library. If pySerial is installed, Python IVI can use it to communicate with instruments via the serial port. </p>
<p> Home page: <i><a rel="nofollow" href="http://pyserial.sourceforge.net/">http://pyserial.sourceforge.net/</a></i></p>
<h2>PYTHON IVI EXAMPLES</h2>
<h3>Connecting to an Instrument</h3>
<p> Connect to an Agilent MSO7104A oscilloscope over LXI (VXI11) on IP address 192.168.1.104: </p>
<pre>
&gt;&gt;&gt; import ivi
&gt;&gt;&gt; mso = ivi.agilent.agilentMSO7104A(&quot;TCPIP::192.168.1.104::INSTR&quot;)
&gt;&gt;&gt; mso.identity.instrument_model
'MSO7104A'
</pre>
<p> Connect to an Agilent E3649A via an HP 2050A GPIB LAN bridge: </p>
<pre>
&gt;&gt;&gt; import ivi
&gt;&gt;&gt; psu = ivi.agilent.agilentE3649A(&quot;TCPIP::192.168.1.105::gpib,5::INSTR&quot;)
&gt;&gt;&gt; psu.identity.instrument_model
'E3649A'
</pre>
<h3>Configuring instruments</h3>
<p> Connect to an Agilent MSO7104A oscilloscope over LXI (VXI11) and configure a channel: </p>
<pre><code>
&gt;&gt;&gt; import ivi &gt;&gt;&gt; mso = ivi.agilent.agilentMSO7104A("TCPIP0::192.168.1.104::INSTR") &gt;&gt;&gt; #mso = ivi.agilent.agilentMSO7104A("USB0::2391::5973::MY********::INSTR") &gt;&gt;&gt; mso.acquisition.time_per_record = 1e-3 &gt;&gt;&gt; mso.trigger.type = 'edge' &gt;&gt;&gt; mso.trigger.source = 'channel1' &gt;&gt;&gt; mso.trigger.coupling = 'dc' &gt;&gt;&gt; mso.trigger.edge.slope = 'positive' &gt;&gt;&gt; mso.trigger.level = 0 &gt;&gt;&gt; mso.channels['channel1'].enabled = True &gt;&gt;&gt; mso.channels['channel1'].offset = 0 &gt;&gt;&gt; mso.channels['channel1'].range = 4 &gt;&gt;&gt; mso.channels['channel1'].coupling = 'dc' &gt;&gt;&gt; mso.measurement.initiate() &gt;&gt;&gt; waveform = mso.channels[0].measurement.fetch_waveform() &gt;&gt;&gt; vpp = mso.channels[0].measurement.fetch_waveform_measurement("voltage_peak_to_peak") &gt;&gt;&gt; phase = mso.channels['channel1'].measurement.fetch_waveform_measurement("phase", "channel2")
</code></pre>
<p> Connect to a Tektronix AWG2021, generate a sinewave with numpy, and transfer it to channel 1: </p>
<p>&gt;&gt;&gt; import ivi &gt;&gt;&gt; from numpy import * &gt;&gt;&gt; #awg = ivi.tektronix.tektronixAWG2021(&#8220;GPIB0::25::INSTR&#8221;) &gt;&gt;&gt; awg = ivi.tektronix.tektronixAWG2021(&#8220;TCPIP0::192.168.1.105::gpib,25::INSTR&#8221;) &gt;&gt;&gt; #awg = ivi.tektronix.tektronixAWG2021(&#8220;ASRL::/dev/ttyUSB0,9600::INSTR&#8221;) &gt;&gt;&gt; n = 128 &gt;&gt;&gt; f = 1 &gt;&gt;&gt; a = 1 &gt;&gt;&gt; wfm = a * sin(2 * pi / n * f * arange(0, n)) &gt;&gt;&gt; awg.outputs[0].arbitrary.create_waveform(wfm) &gt;&gt;&gt; awg.outputs[0].arbitrary.gain = 2.0 &gt;&gt;&gt; awg.outputs[0].arbitrary.gain = 0.0 &gt;&gt;&gt; arb.arbitrary.sample_rate = 128e6 &gt;&gt;&gt; awg.outputs[0].enabled = True</p>
<p> Connect to an Agilent E3649A and configure an output: </p>
<p>&gt;&gt;&gt; import ivi &gt;&gt;&gt; #psu = ivi.agilent.agilentE3649A(&#8220;GPIB0::5::INSTR&#8221;) &gt;&gt;&gt; psu = ivi.agilent.agilentE3649A(&#8220;TCPIP0::192.168.1.105::gpib,5::INSTR&#8221;) &gt;&gt;&gt; #psu = ivi.agilent.agilentE3649A(&#8220;ASRL::/dev/ttyUSB0,9600::INSTR&#8221;) &gt;&gt;&gt; psu.outputs[0].configure_range(&#8216;voltage&#8217;, 12) &gt;&gt;&gt; psu.outputs[0].voltage_level = 12.0 &gt;&gt;&gt; psu.outputs[0].current_limit = 1.0 &gt;&gt;&gt; psu.outputs[0].ovp_limit = 14.0 &gt;&gt;&gt; psu.outputs[0].ovp_enabled = True &gt;&gt;&gt; psu.outptus[0].enabled = True</p>
<h2>IVI &#8212; IVI DRIVER</h2>
<p> This module provides the base functionality of an IVI instrument driver.</p>
<h3>Functions and Exceptions</h3>
<dl>
<dt><code>exception ivi.IviException</code></p>
<dd> Exception raised on various occasions; argument is a string describing what is wrong.</dl>
<h3><code>DriverOperation</code> class</h3>
<dl>
<dt><code>class ivi.DriverOperation(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Inherent IVI methods for driver operation</dl>
<h3><code>DriverIdentity</code> class</h3>
<dl>
<dt><code>class ivi.DriverIdentity(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Inherent IVI methods for identification</dl>
<h3><code>DriverUtility</code> class</h3>
<dl>
<dt><code>class ivi.DriverUtility(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Inherent IVI utility methods</dl>
<h3><code>Driver</code> class</h3>
<dl>
<dt><code>class ivi.Driver(resource=None, id_query=False, reset=False, *args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.DriverOperation</code>, <code>ivi.ivi.DriverIdentity</code>, <code>ivi.ivi.DriverUtility</code> </p>
<p> Inherent IVI methods for all instruments</p>
<dt><code>doc(obj=None, itm=None, docs=None, prefix=None)</code></p>
<dd> Python IVI documentation generator</p>
<dt><code>help(itm=None, complete=False, indent=0)</code></p>
<dd> Python IVI help system</p>
<dt><code>ivi.close</code></p>
<dd> When the user finishes using a Python IVI driver, the user should call either the Close method or __del__. Note that __del__ will call close automatically. </p>
<p> This function also does the following:</p>
<dt>&bull;</p>
<dd> Prevents the user from calling other functions in the driver that access the instrument until the user calls the Initialize function again.</p>
<dt>&bull;</p>
<dd> May deallocate internal resources used by the IVI session.</p>
<dt><code>driver_operation.cache</code></p>
<dd> If True, the specific driver caches the value of attributes, and the IVI specific driver keeps track of the current instrument settings so that it can avoid sending redundant commands to the instrument. If False, the specific driver does not cache the value of attributes. </p>
<p> The default value is True. When the user opens an instrument session through an IVI class driver or uses a logical name to initialize a specific driver, the user can override this value by specifying a value in the IVI configuration store. The Initialize function allows the user to override both the default value and the value that the user specifies in the IVI configuration store.</p>
<dt><code>driver_operation.clear_interchange_warnings</code></p>
<dd> This function clears the list of interchangeability warnings that the IVI specific driver maintains. </p>
<p> When this function is called on an IVI class driver session, the function clears the list of interchangeability warnings that the class driver and the specific driver maintain. </p>
<p> Refer to the Interchange Check attribute for more information on interchangeability checking.</p>
<dt><code>driver_operation.driver_setup</code></p>
<dd> Returns the driver setup string that the user specified in the IVI configuration store when the instrument driver session was initialized or passes in the OptionString parameter of the Initialize function. Refer to Section 6.14, Initialize, for the restrictions on the format of the driver setup string. </p>
<p> The string that this attribute returns does not have a predefined maximum length.</p>
<dt><code>driver_operation.get_next_coercion_record</code></p>
<dd> If the Record Value Coercions attribute is set to True, the IVI specific driver keeps a list of all value coercions it makes on integer and floating point attributes. This function obtains the coercion information associated with the IVI session. It retrieves and clears the oldest instance in which the specific driver coerced a value the user specified to another value. </p>
<p> The function returns an empty string in the CoercionRecord parameter if no coercion records remain for the session. </p>
<p> The coercion record string shall contain the following information:</p>
<dt>&bull;</p>
<dd> The name of the attribute that was coerced. This can be the generic name, the COM property name, or the C defined constant.</p>
<dt>&bull;</p>
<dd> If the attribute applies to a repeated capability, the name of the virtual or physical repeated capability identifier.</p>
<dt>&bull;</p>
<dd> The value that the user specified for the attribute.</p>
<dt>&bull;</p>
<dd> The value to which the attribute was coerced. </p>
<p> A recommended format for the coercion record string is as follows: </p>
<pre>
&quot; Attribute &quot; + &lt;attribute name&gt; + [&quot; on &lt;repeated capability&gt; &quot; +
&lt;repeated capability identifier&gt;] + &quot; was coerced from &quot; +
&lt;desiredVal&gt; + &quot; to &quot; + &lt;coercedVal&gt;
</pre>
<p> . </p>
<p> And example coercion record string is as follows: </p>
<pre>
Attribute TKTDS500_ATTR_VERTICAL_RANGE on channel ch1 was coerced from
9.0 to 10.0.
</pre>
<dt><code>driver_operation.get_next_interchange_warning</code></p>
<dd> If the Interchange Check attribute is set to True, the IVI specific driver keeps a list of all interchangeability warnings that it encounters. This function returns the interchangeability warnings associated with the IVI session. It retrieves and clears the oldest interchangeability warning from the list. Interchangeability warnings indicate that using the application with a different instrument might cause different behavior. </p>
<p> When this function is called on an IVI class driver session, it may return interchangeability warnings generated by the IVI class driver as well as interchangeability warnings generated by the IVI specific driver. The IVI class driver determines the relative order in which the IVI class driver warnings are returned in relation to the IVI specific driver warnings. </p>
<p> The function returns an empty string in the InterchangeWarning parameter if no interchangeability warnings remain for the session. </p>
<p> Refer to the Interchange Check attribute for more information on interchangeability checking.</p>
<dt><code>driver_operation.interchange_check</code></p>
<dd> If True, the specific driver performs interchangeability checking. If the Interchange Check attribute is enabled, the specific driver maintains a record of each interchangeability warning that it encounters. The user calls the Get Next Interchange Warning function to extract and delete the oldest interchangeability warning from the list. Refer to Section 6.11, Get Next Interchange Warning, Section 6.2, Clear Interchange Warnings, and Section 6.18, Reset Interchange Check, for more information. If False, the specific driver does not perform interchangeability checking. </p>
<p> If the user opens an instrument session through an IVI class driver and the Interchange Check attribute is enabled, the IVI class driver may perform additional interchangeability checking. The IVI class driver maintains a list of the interchangeability warnings that it encounters. The user can retrieve both class driver interchangeability warnings and specific driver interchangeability warnings by calling the Get Next Interchange Warning function on the class driver session. </p>
<p> If the IVI specific driver does not implement interchangeability checking, the specific driver returns the Value Not Supported error when the user attempts to set the Interchange Check attribute to True. If the specific driver does implement interchangeability checking and the user opens an instrument session through an IVI class driver, the IVI class driver accepts True as a valid value for the Interchange Check attribute even if the class driver does not implement interchangeability checking capabilities of its own. </p>
<p> The default value is False. If the user opens an instrument session through an IVI class driver or initializes an IVI specific driver with a logical name, the user can override this value in the IVI configuration store. The Initialize function allows the user to override both the default value and the value that the userspecifies in the IVI configuration store.</p>
<dt><code>driver_operation.invalidate_all_attributes</code></p>
<dd> This function invalidates the cached values of all attributes for the session.</p>
<dt><code>driver_operation.io_resource_descriptor</code></p>
<dd> Returns the resource descriptor that the user specified for the physical device. The user specifies the resource descriptor by editing the IVI configuration store or by passing a resource descriptor to the Initialize function of the specific driver. Refer to Section 6.14, Initialize, for the restrictions on the contents of the resource descriptor string. </p>
<p> The string that this attribute returns contains a maximum of 256 characters including the NULL character.</p>
<dt><code>driver_operation.logical_name</code></p>
<dd> Returns the IVI logical name that the user passed to the Initialize function. If the user initialized the IVI specific driver directly and did not pass a logical name, then this attribute returns an empty string. Refer to IVI-3.5: Configuration Server Specification for restrictions on the format of IVI logical names. </p>
<p> The string that this attribute returns contains a maximum of 256 characters including the NULL character.</p>
<dt><code>driver_operation.query_instrument_status</code></p>
<dd> If True, the IVI specific driver queries the instrument status at the end of each user operation. If False, the IVI specific driver does not query the instrument status at the end of each user operation. Querying the instrument status is very useful for debugging. After validating the program, the user can set this attribute to False to disable status checking and maximize performance. The user specifies this value for the entire IVI driver session. </p>
<p> The default value is False. When the user opens an instrument session through an IVI class driver or uses a logical name to initialize an IVI specific driver, the user can override this value by specifying a value in the IVI configuration store. The Initialize function allows the user to override both the default value and the value that the user specifies in the IVI configuration store.</p>
<dt><code>driver_operation.range_check</code></p>
<dd> If True, the IVI specific driver validates attribute values and function parameters. If False, the IVI specific driver does not validate attribute values and function parameters. </p>
<p> If range check is enabled, the specific driver validates the parameter values that users pass to driver functions. Validating attribute values and function parameters is useful for debugging. After validating the program, the user can set this attribute to False to disable range checking and maximize performance. The default value is True. When the user opens an instrument session through an IVI class driver or uses a logical name to initialize an IVI specific driver, the user can override this value by specifying a value in the IVI configuration store. The Initialize function allows the user to override both the default value and the value that the user specifies in the IVI configuration store.</p>
<dt><code>driver_operation.record_coercions</code></p>
<dd> If True, the IVI specific driver keeps a list of the value coercions it makes for ViInt32 and ViReal64 attributes. If False, the IVI specific driver does not keep a list of the value coercions it makes for ViInt32 and ViReal64 attributes. </p>
<p> If the Record Value Coercions attribute is enabled, the specific driver maintains a record of each coercion. The user calls the Get Next Coercion Record function to extract and delete the oldest coercion record from the list. Refer to Section 6.10, Get Next Coercion Record, for more information. </p>
<p> If the IVI specific driver does not implement coercion recording, the specific driver returns the Value Not Supported error when the user attempts to set the Record Value Coercions attribute to True. </p>
<p> The default value is False. When the user opens an instrument session through an IVI class driver or uses a logical name to initialize a IVI specific driver, the user can override this value by specifying a value in the IVI configuration store. The Initialize function allows the user to override both the default value and the value that the user specifies in the IVI configuration store.</p>
<dt><code>driver_operation.reset_interchange_check</code></p>
<dd> This function resets the interchangeability checking algorithms of the IVI specific driver so that specific driver functions that execute prior to calling this function have no effect on whether future calls to the specific driver generate interchangeability warnings. </p>
<p> When developing a complex test system that consists of multiple test modules, it is generally a good idea to design the test modules so that they can run in any order. To do so requires ensuring that each test module completely configures the state of each instrument it uses. If a particular test module does not completely configure the state of an instrument, the state of the instrument depends on the configuration from a previously executed test module. If the test modules execute in a different order, the behavior of the instrument and therefore the entire test module is likely to change. This change in behavior is generally instrument specific and represents an interchangeability problem. </p>
<p> Users can use this function to test for such cases. By calling this function at the beginning of a test module, users can determine whether the test module has dependencies on the operation of previously executed test modules. Any interchangeability warnings that occur after the user calls this function indicate that the section of the test program that executes after this function and prior to the generation of the warning does not completely configure the instrument and that the user is likely to experience different behavior if the user changes the execution order of the test modules or if the user changes instruments. </p>
<p> Note: This function does not clear interchangeability warnings from the list of interchangeability warnings. To guarantee that the Get Next Interchange Warning function returns interchangeability warnings that occur only after the program calls function, the user must clear the list of interchangeability warnings by calling the Clear Interchange Warnings function. </p>
<p> Refer to the Interchange Check attribute for more information on interchangeability checking.</p>
<dt><code>driver_operation.simulate</code></p>
<dd> If True, the IVI specific driver simulates instrument driver I/O operations. If False, the IVI specific driver communicates directly with the instrument. </p>
<p> If simulation is enabled, the specific driver functions do not perform instrument I/O. For output parameters that represent instrument data, the specific driver functions return simulated values. </p>
<p> The default value is False. When the user opens an instrument session through an IVI class driver or uses a logical name to initialize an IVI specific driver, the user can override this value by specifying a value in the IVI configuration store. The Initialize function allows the user to override both the default value and the value that the user specifies in the IVI configuration store.</p>
<dt><code>identity.description</code></p>
<dd> Returns a brief description of the IVI software component. </p>
<p> The string that this attribute returns has no maximum size.</p>
<dt><code>identity.get_group_capabilities</code></p>
<dd> Returns a list of names of class capability groups that the IVI specific driver implements. The items in the list are capability group names that the IVI class specifications define. The list is returned as a list of strings. </p>
<p> If the IVI specific driver does not comply with an IVI class specification, the specific driver returns an array with zero elements.</p>
<dt><code>identity.get_supported_instrument_models</code></p>
<dd> Returns a list of names of instrument models with which the IVI specific driver is compatible. The list is returned as a list of strings. For example, this attribute might return the strings &quot;TKTDS3012&quot;, &quot;TKTDS3014&quot;, and &quot;TKTDS3016&quot; . </p>
<p> It is not necessary for the string to include the abbreviation for the manufacturer if it is the same for all models. In the example above, it is valid for the attribute to return the strings &quot;TDS3012&quot;, &quot;TDS3014&quot;, and &quot;TDS3016&quot;.</p>
<dt><code>identity.group_capabilities</code></p>
<dd> Returns a comma-separated list that identifies the class capability groups that the IVI specific driver implements. The items in the list are capability group names that the IVI class specifications define. The string has no white space except for white space that might be embedded in a capability group name. </p>
<p> If the IVI specific driver does not comply with an IVI class specification, the specific driver returns an empty string as the value of this attribute. </p>
<p> The string that this attribute returns does not have a predefined maximum length.</p>
<dt><code>identity.identifier</code></p>
<dd> Returns the case-sensitive unique identifier of the IVI software component. The string that this attribute returns contains a maximum of 32 characters including the NULL character.</p>
<dt><code>identity.instrument_firmware_revision</code></p>
<dd> Returns an instrument specific string that contains the firmware revision information of the physical instrument. The IVI specific driver returns the value it queries from the instrument as the value of this attribute or a string indicating that it cannot query the instrument identity. </p>
<p> In some cases, it is not possible for the specific driver to query the firmware revision of the instrument. This can occur when the Simulate attribute is set to True or if the instrument is not capable of returning the firmware revision. For these cases, the specific driver returns defined strings for this attribute. If the Simulate attribute is set to True, the specific driver returns &quot;Not available while simulating&quot; as the value of this attribute. If the instrument is not capable of returning the firmware version and the Simulate attribute is set to False, the specific driver returns &quot;Cannot query from instrument&quot; as the value of this attribute. </p>
<p> The string that this attribute returns does not have a predefined maximum length.</p>
<dt><code>identity.instrument_manufacturer</code></p>
<dd> Returns the name of the manufacturer of the instrument. The IVI specific driver returns the value it queries from the instrument as the value of this attribute or a string indicating that it cannot query the instrument identity. </p>
<p> In some cases, it is not possible for the specific driver to query the manufacturer of the instrument. This can occur when the Simulate attribute is set to True or if the instrument is not capable of returning the manufacturer. For these cases, the specific driver returns defined strings for this attribute. If the Simulate attribute is set to True, the specific driver returns &quot;Not available while simulating&quot; as the value of this attribute. If the instrument is not capable of returning the manufacturer and the Simulate attribute is set to False, the specific driver returns &quot;Cannot query from instrument&quot; as the value of this attribute. </p>
<p> The string that this attribute returns does not have a predefined maximum length.</p>
<dt><code>identity.instrument_model</code></p>
<dd> Returns the model number or name of the physical instrument. The IVI specific driver returns the value it queries from the instrument or a string indicating that it cannot query the instrument identity. </p>
<p> In some cases, it is not possible for the specific driver to query the model of the instrument. This can occur when the Simulate attribute is set to True or if the instrument is not capable of returning the model. For these cases, the specific driver returns defined strings for this attribute. If the Simulate attribute is set to True, the specific driver returns &quot;Not available while simulating&quot; as the value of this attribute. If the instrument is not capable of returning the model and the Simulate attribute is set to False, the specific driver returns &quot;Cannot query from instrument&quot; as the value of this attribute. </p>
<p> The string that this attribute returns does not have a predefined maximum length.</p>
<dt><code>identity.revision</code></p>
<dd> Returns version information about the IVI software component. Refer to Section 3.1.2.2, Additional Compliance Rules for Revision String Attributes, for additional rules regarding this attribute. </p>
<p> The string that this attribute returns has no maximum size.</p>
<dt><code>identity.specification_major_version</code></p>
<dd> Returns the major version number of the class specification in accordance with which the IVI software component was developed. The value is a positive integer value. </p>
<p> If the software component is not compliant with a class specification, the software component returns zero as the value of this attribute.</p>
<dt><code>identity.specification_minor_version</code></p>
<dd> Returns the minor version number of the class specification in accordance with which the IVI software component was developed. The value is a positive integer value. </p>
<p> If the software component is not compliant with a class specification, the software component returns zero as the value of this attribute.</p>
<dt><code>identity.supported_instrument_models</code></p>
<dd> Returns a comma-separated list of names of instrument models with which the IVI specific driver is compatible. The string has no white space except possibly embedded in the instrument model names. An example of a string that this attribute might return is &quot;TKTDS3012,TKTDS3014,TKTDS3016&quot;. </p>
<p> It is not necessary for the string to include the abbreviation for the manufacturer if it is the same for all models. In the example above, it is valid for the attribute to return the string &quot;TDS3012,TDS3014,TDS3016&quot;. </p>
<p> The string that this attribute returns does not have a predefined maximum length.</p>
<dt><code>identity.vendor</code></p>
<dd> Returns the name of the vendor that supplies the IVI software component. </p>
<p> The string that this attribute returns has no maximum size.</p>
<dt><code>ivi.initialize</code></p>
<dd> The user must call the Initialize function prior to calling other IVI driver functions that access the instrument. The Initialize function is called automatically by the constructor if a resource string is passed as the first argument to the constructor. </p>
<p> If simulation is disabled when the user calls the Initialize function, the function performs the following actions:</p>
<dt>&bull;</p>
<dd> Opens and configures an I/O session to the instrument.</p>
<dt>&bull;</p>
<dd> If the user passes True for the IdQuery parameter, the function queries the instrument for its ID and verifies that the IVI specific driver supports the particular instrument model. If the instrument cannot return its ID, the specific driver returns the ID Query Not Supported warning.</p>
<dt>&bull;</p>
<dd> If the user passes True for the Reset parameter, the function places the instrument in a known state. In an IEEE 488.2 instrument, the function sends the command string &quot; </p>
<pre>
*
</pre>
<p> RST&quot; to the instrument. If the instrument cannot perform a reset, the IVI specific driver returns the Reset Not Supported warning.</p>
<dt>&bull;</p>
<dd> Configures instrument options on which the IVI specific driver depends. For example, a specific driver might enable or disable headers or enable binary mode for waveform transfers.</p>
<dt>&bull;</p>
<dd>
<dt><code>Performs the following operations in the given order:</code></p>
<dd>
<dt>1.</p>
<dd> Disables the class extension capability groups that the IVI specific driver does not implement.</p>
<dt>2.</p>
<dd> If the class specification with which the IVI specific driver is compliant defines initial values for attributes, this function sets the attributes to the values that the class specification defines.</p>
<dt>3.</p>
<dd> If the ResourceName parameter is a logical name, the IVI specific driver configures the initial settings for the specific driver and instrument based on the configuration of the logical name in the IVI configuration store. </p>
<p> If simulation is enabled when the user calls the Initialize function, the function performs the following actions:</p>
<dt>&bull;</p>
<dd> If the user passes True for the IdQuery parameter and the instrument cannot return its ID, the IVI specific driver returns the ID Query Not Supported warning.</p>
<dt>&bull;</p>
<dd> If the user passes True for the Reset parameter and the instrument cannot perform a reset, the IVI specific driver returns the Reset Not Supported warning.</p>
<dt>&bull;</p>
<dd> If the ResourceName parameter is a logical name, the IVI specific driver configures the initial settings for the specific driver based on the configuration of the logical name in the IVI configuration store. </p>
<p> Some instrument driver operations require or take into account information from the IVI configuration store. Examples of such information are virtual repeated capability name mappings and the value of certain inherent attributes. An IVI driver shall retrieve all the information for a session from the IVI configuration store during the Initialization function. The IVI driver shall not read any information from the IVI configuration store for a session after the Initialization function completes. Refer to Section 3.2.3, Instantiating the Right Configuration Store From Software Modules, of IVI-3.5: Configuration Server Specification for details on how to correctly instantiate the configuration store. </p>
<p> The ResourceName parameter must contain either a logical name that is defined in the IVI configuration store or an instrument specific string that identifies the I/O address of the instrument, such as a VISA resource descriptor string. Refer to IVI-3.5: Configuration Server Specification for restrictions on the format of IVI logical names. Refer to the VXIplug&amp;play specifications for the grammar of VISA resource descriptor strings. </p>
<p> Example resource strings: </p>
<pre>
'TCPIP::10.0.0.1::INSTR'
'TCPIP0::10.0.0.1::INSTR'
'TCPIP::10.0.0.1::gpib,5::INSTR'
'TCPIP0::10.0.0.1::gpib,5::INSTR'
'TCPIP0::10.0.0.1::usb0::INSTR'
'TCPIP0::10.0.0.1::usb0[1234::5678::MYSERIAL::0]::INSTR'
'USB::1234::5678::INSTR'
'USB::1234::5678::SERIAL::INSTR'
'USB0::0x1234::0x5678::INSTR'
'USB0::0x1234::0x5678::SERIAL::INSTR'
'GPIB::10::INSTR'
'GPIB0::10::INSTR'
'ASRL1::INSTR'
'ASRL::COM1,9600,8n1::INSTR'
'ASRL::/dev/ttyUSB0,9600::INSTR'
'ASRL::/dev/ttyUSB0,9600,8n1::INSTR'
</pre>
<p> The user can use additional parameters to specify the initial values of certain IVI inherent attributes for the session. The following table lists the inherent attributes that the user can set through these named parameters. The user does not have to specify all or any of the attributes. If the user does not specify the initial value of an inherent attribute, the initial value of the attribute depends on the value of the ResourceName parameter:</p>
<dt>&bull;</p>
<dd> If the ResourceName parameter contains an IVI logical name, the IVI specific driver configures the initial settings based on the configuration of the logical name in the IVI configuration store.</p>
<dt>&bull;</p>
<dd> If the ResourceName parameter contains a resource descriptor string that identifies the I/O address of the instrument, the IVI specific driver sets inherent attributes to their default initial values. The following table shows the default initial value for each attribute. </p>
<p> The following table lists the IVI inherent attributes that the user can set, their default initial values, and the name that represents each attribute. These options are passed to the initialize function or the constructor as key-value pairs. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Attribute </td>
<td> Default Inital Value </td>
<td> Options String Name
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Range Check </td>
<td> True </td>
<td> range_check
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Query Instrument Status </td>
<td> False </td>
<td> query_instr_status
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Cache </td>
<td> True </td>
<td> cache
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Simulate </td>
<td> False </td>
<td> simulate
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Record Value Coercions </td>
<td> False </td>
<td> record_coercions
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Interchange Check </td>
<td> False </td>
<td> interchange_check
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Driver Setup </td>
<td> &#8221; </td>
<td> driver_setup
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Prefer PyVISA </td>
<td> False </td>
<td> prefer_pyvisa
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Each IVI specific driver defines it own meaning and valid values for the Driver Setup attribute. Many specific drivers ignore the value of the Driver Setup attribute. Other specific drivers use the Driver Setup string to configure instrument specific features at initialization. For example, if a specific driver supports a family of instrument models, the driver can use the Driver Setup attribute to allow the user to specify a particular instrument model to simulate. </p>
<p> If the user attempts to initialize the instrument a second time without first calling the Close function, the Initialize function returns the Already Initialized error.</p>
<dt><code>ivi.initialized</code></p>
<dd> Returns a value that indicates whether the IVI specific driver is in the initialized state. After the specific driver is instantiated and before the Initialize function successfully executes, this attribute returns False. After the Initialize function successfully executes and prior to the execution of the Close function, this attribute returns True. After the Close function executes, this attribute returns False. </p>
<p> The Initialized attribute is one of the few IVI specific driver attributes that can be accessed while the specific driver is not in the initialized state. All the attributes of an IVI specific driver that can be accessed while the specific driver is not in the initialized state are listed below.</p>
<dt>&bull;</p>
<dd> Component Class Spec Major Version</p>
<dt>&bull;</p>
<dd> Component Class Spec Minor Version</p>
<dt>&bull;</p>
<dd> Component Description</p>
<dt>&bull;</p>
<dd> Component Prefix</p>
<dt>&bull;</p>
<dd> Component Identifier</p>
<dt>&bull;</p>
<dd> Component Revision</p>
<dt>&bull;</p>
<dd> Component Vendor</p>
<dt>&bull;</p>
<dd> Initialized</p>
<dt>&bull;</p>
<dd> Supported Instrument Models</p>
<dt><code>utility.disable</code></p>
<dd> The Disable operation places the instrument in a quiescent state as quickly as possible. In a quiescent state, an instrument has no or minimal effect on the external system to which it is connected. The Disable operation might be similar to the Reset operation in that it places the instrument in a known state. However, the Disable operation does not perform the other operations that the Reset operation performs such as configuring the instrument options on which the IVI specific driver depends. For some instruments, the disable function may do nothing. </p>
<p> The IVI class specifications define the exact behavior of this function for each instrument class. Refer to the IVI class specifications for more information on the behavior of this function.</p>
<dt><code>utility.error_query</code></p>
<dd> Queries the instrument and returns instrument specific error information. </p>
<p> Generally, the user calls this function after another function in the IVI driver returns the Instrument Status error. The IVI specific driver returns the Instrument Status error when the instrument indicates that it encountered an error and its error queue is not empty. Error Query extracts an error out of the instrument&#8217;s error queue. </p>
<p> For instruments that have status registers but no error queue, the IVI specific driver emulates an error queue in software. </p>
<p> The method returns a tuple containing the error code and error message.</p>
<dt><code>utility.lock_object</code></p>
<dd> This function obtains a multithread lock for this instance of the driver. Before it does so, Lock Session waits until all other execution threads have released their locks or for the length of time specified by the maximum time parameter, whichever come first. The type of lock obtained depends upon the parameters passed to the specific driver constructor. </p>
<p> The user can use Lock Session with IVI specific drivers to protect a section of code that requires exclusive access to the instrument. This occurs when the user takes multiple actions that affect the instrument and the user wants to ensure that other execution threads do not disturb the instrument state until all the actions execute. For example, if the user sets various instrument attributes and then triggers a measurement, the user must ensure no other execution thread modifies the attribute values until the user finishes taking the measurement. </p>
<p> It is important to note that this lock is not related to I/O locks such as the VISA resource locking mechanism. </p>
<p> The user can safely make nested calls to Lock Session within the same thread. To completely unlock the session, the user must balance each call to Lock Session with a call to Unlock Session. Calls to Lock Session must always obtain the same lock that is used internally by the IVI driver to guard individual method calls.</p>
<dt><code>utility.reset</code></p>
<dd> This function performs the following actions:</p>
<dt>&bull;</p>
<dd> Places the instrument in a known state. In an IEEE 488.2 instrument, the Reset function sends the command string <code>*RST</code> to the instrument.</p>
<dt>&bull;</p>
<dd> Configures instrument options on which the IVI specific driver depends. A specific driver might enable or disable headers or enable binary mode for waveform transfers. </p>
<p> The user can either call the Reset function separately or specify that it be called from the Initialize function. The Initialize function performs additional operations after performing the reset operation to place the instrument in a state more suitable for interchangeable programming. To reset the device and perform these additional operations, call the Reset With Defaults function instead of the Reset function.</p>
<dt><code>utility.reset_with_defaults</code></p>
<dd> The Reset With Defaults function performs the same operations that the Reset function performs and then performs the following additional operations in the specified order:</p>
<dt>&bull;</p>
<dd> Disables the class extension capability groups that the IVI specific driver implements.</p>
<dt>&bull;</p>
<dd> If the class specification with which the IVI specific driver is compliant defines initial values for attributes, this function sets those attributes to the initial values that the class specification defines.</p>
<dt>&bull;</p>
<dd> Configures the initial settings for the specific driver and instrument based on the information retrieved from the IVI configuration store when the instrument driver session was initialized. </p>
<p> Notice that the Initialize function also performs these functions. To place the instrument and the IVI specific driver in the exact same state that they attain when the user calls the Initialize function, the user must first call the Close function and then the Initialize function.</p>
<dt><code>utility.self_test</code></p>
<dd> Causes the instrument to perform a self test. Self Test waits for the instrument to complete the test. It then queries the instrument for the results of the self test and returns the results to the user. </p>
<p> If the instrument passes the self test, this function returns the tuple: </p>
<pre>
(0, 'Self test passed')
</pre>
<p> Otherwise, the function returns a tuple of the result code and message.</p>
<dt><code>utility.unlock_object</code></p>
<dd> This function releases a lock that the Lock Session function acquires. </p>
<p> Refer to Lock Session for additional information on IVI session locks.</dl>
<h3>Helper Classes</h3>
<h3><code>PropertyCollection</code> class</h3>
<dl>
<dt><code>class ivi.PropertyCollection</code></p>
<dd> A building block to create hierarchical trees of methods and properties</p>
<dt><code>_add_method(name, f=None, doc=None)</code></p>
<dd> Add a managed method</p>
<dt><code>_add_property(name, fget=None, fset=None, fdel=None, doc=None)</code></p>
<dd> Add a managed property</p>
<dt><code>_del_property(name)</code></p>
<dd> Remove managed property or method</p>
<dt><code>_lock(lock=True)</code></p>
<dd> Set lock state to prevent creation or deletion of unmanaged members</p>
<dt><code>_unlock()</code></p>
<dd> Unlock object to allow creation or deletion of unmanaged members, equivalent to _lock(False)</dl>
<h3><code>IndexedPropertyCollection</code> class</h3>
<dl>
<dt><code>class ivi.IndexedPropertyCollection</code></p>
<dd> A building block to create hierarchical trees of methods and properties with an index that is converted to a parameter</p>
<dt><code>_add_method(name, f=None, doc=None, props=None, docs=None)</code></p>
<dd> Add a managed method</p>
<dt><code>_add_property(name, fget=None, fset=None, fdel=None, doc=None, props=None, docs=None)</code></p>
<dd> Add a managed property</p>
<dt><code>_add_sub_method(sub, name, f=None, doc=None)</code></p>
<dd> Add a sub-method (equivalent to _add_method(&#8216;sub.name&#8217;, &#8230;))</p>
<dt><code>_add_sub_property(sub, name, fget=None, fset=None, fdel=None, doc=None)</code></p>
<dd> Add a sub-property (equivalent to _add_property(&#8216;sub.name&#8217;, &#8230;))</p>
<dt><code>_build_obj(props, docs, i)</code></p>
<dd> Build a tree of PropertyCollection objects with the proper index associations</p>
<dt><code>_del_property(name)</code></p>
<dd> Delete property</p>
<dt><code><a href="/docs/linux/man/l-_set_list/">_set_list</a>(l)</code></p>
<dd> Set a list of allowable indicies as an associative array</dl>
<h2>IVI.SCOPE &#8212; OSCILLOSCOPE CLASS</h2>
<p> This module provides the base functionality for Oscilloscopes.</p>
<h3>Functions and Exceptions</h3>
<dl>
<dt><code>exception ivi.scope.IviException</code></p>
<dd> Exception raised on various occasions; argument is a string describing what is wrong.</dl>
<h3><code>Base</code> class</h3>
<dl>
<dt><code>class ivi.scope.Base(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Base IVI methods for all oscilloscopes</p>
<dt><code>acquisition.configure_record</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.3.4</i> </p>
<p> This function configures the most commonly configured attributes of the oscilloscope acquisition sub-system. These attributes are the time per record, minimum record length, and the acquisition start time.</p>
<dt><code>acquisition.number_of_points_minimum</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.8</i> </p>
<p> Specifies the minimum number of points the end-user requires in the waveform record for each channel. The instrument driver uses the value the end-user specifies to configure the record length that the oscilloscope uses for waveform acquisition. If the instrument cannot support the requested record length, the driver shall configure the instrument to the closest bigger record length. The Horizontal Record Length attribute returns the actual record length.</p>
<dt><code>acquisition.record_length</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.9</i> </p>
<p> Returns the actual number of points the oscilloscope acquires for each channel. The value is equal to or greater than the minimum number of points the end-user specifies with the Horizontal Minimum Number of Points attribute. </p>
<p> Note: Oscilloscopes may use different size records depending on the value the user specifies for the Acquisition Type attribute.</p>
<dt><code>acquisition.sample_rate</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.10</i> </p>
<p> Returns the effective sample rate of the acquired waveform using the current configuration. The units are samples per second.</p>
<dt><code>acquisition.start_time</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.1</i> </p>
<p> Specifies the length of time from the trigger event to the first point in the waveform record. If the value is positive, the first point in the waveform record occurs after the trigger event. If the value is negative, the first point in the waveform record occurs before the trigger event. The units are seconds.</p>
<dt><code>acquisition.time_per_record</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.11</i> </p>
<p> Specifies the length of time that corresponds to the record length. The units are seconds.</p>
<dt><code>acquisition.type</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.3</i> </p>
<p> Specifies how the oscilloscope acquires data and fills the waveform record. </p>
<p> Values: * &#8216;normal&#8217; * &#8216;high_resolution&#8217; * &#8216;average&#8217; * &#8216;peak_detect&#8217; * &#8216;envelope&#8217;</p>
<dt><code>channels[].configure</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.3.6</i> </p>
<p> This function configures the most commonly configured attributes of the oscilloscope channel sub-system. These attributes are the range, offset, coupling, probe attenuation, and whether the channel is enabled.</p>
<dt><code>channels[].configure_characteristics</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.3.8</i> </p>
<p> This function configures the attributes that control the electrical characteristics of the channel. These attributes are the input impedance and the maximum frequency of the input signal.</p>
<dt><code>channels[].coupling</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.23</i> </p>
<p> Specifies how the oscilloscope couples the input signal for the channel. </p>
<p> Values:</p>
<dt>&bull;</p>
<dd> &#8216;ac&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;dc&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;gnd&#8217;</p>
<dt><code>channels[].enabled</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.5</i> </p>
<p> If set to True, the oscilloscope acquires a waveform for the channel. If set to False, the oscilloscope does not acquire a waveform for the channel.</p>
<dt><code>channels[].input_frequency_max</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.13</i> </p>
<p> Specifies the maximum frequency for the input signal you want the instrument to accommodate without attenuating it by more than 3dB. If the bandwidth limit frequency of the instrument is greater than this maximum frequency, the driver enables the bandwidth limit. This attenuates the input signal by at least 3dB at frequencies greater than the bandwidth limit.</p>
<dt><code>channels[].input_impedance</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.12</i> </p>
<p> Specifies the input impedance for the channel in Ohms. </p>
<p> Common values are 50.0, 75.0, and 1,000,000.0.</p>
<dt><code>channels[].measurement.fetch_waveform</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.3.13</i> </p>
<p> This function returns the waveform the oscilloscope acquires for the specified channel. The waveform is from a previously initiated acquisition. </p>
<p> You use the Initiate Acquisition function to start an acquisition on the channels that the end-user configures with the Configure Channel function. The oscilloscope acquires waveforms on the concurrently enabled channels. If the channel is not enabled for the acquisition, this function returns the Channel Not Enabled error. </p>
<p> Use this function only when the acquisition mode is Normal, Hi Res, or Average. If the acquisition type is not one of the listed types, the function returns the Invalid Acquisition Type error. </p>
<p> You use the Acquisition Status function to determine when the acquisition is complete. You must call this function separately for each enabled channel to obtain the waveforms. </p>
<p> You can call the Read Waveform function instead of the Initiate Acquisition function. The Read Waveform function starts an acquisition on all enabled channels, waits for the acquisition to complete, and returns the waveform for the specified channel. You call this function to obtain the waveforms for each of the remaining channels. </p>
<p> The return value is a list of (x, y) tuples that represent the time and voltage of each data point. The y point may be NaN in the case that the oscilloscope could not sample the voltage. </p>
<p> The end-user configures the interpolation method the oscilloscope uses with the Acquisition.Interpolation property. If interpolation is disabled, the oscilloscope does not interpolate points in the waveform. If the oscilloscope cannot sample a value for a point in the waveform, the driver sets the corresponding element in the waveformArray to an IEEE-defined NaN (Not a Number) value. Check for this value with math.isnan() or numpy.isnan(). </p>
<p> This function does not check the instrument status. Typically, the end-user calls this function only in a sequence of calls to other low-level driver functions. The sequence performs one operation. The end-user uses the low-level functions to optimize one or more aspects of interaction with the instrument. Call the Error Query function at the conclusion of the sequence to check the instrument status.</p>
<dt><code>channels[].measurement.read_waveform</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.3.16</i> </p>
<p> This function initiates an acquisition on the channels that the end-user configures with the Configure Channel function. If the channel is not enabled for the acquisition, this function returns Channel Not Enabled error. It then waits for the acquisition to complete, and returns the waveform for the channel the end-user specifies. If the oscilloscope did not complete the acquisition within the time period the user specified with the max_time parameter, the function returns the Max Time Exceeded error. </p>
<p> Use this function only when the acquisition mode is Normal, Hi Res, or Average. If the acquisition type is not one of the listed types, the function returns the Invalid Acquisition Type error. </p>
<p> You call the Fetch Waveform function to obtain the waveforms for each of the remaining enabled channels without initiating another acquisition. After this function executes, each element in the WaveformArray parameter is either a voltage or a value indicating that the oscilloscope could not sample a voltage. </p>
<p> The end-user configures the interpolation method the oscilloscope uses with the Acquisition.Interpolation property. If interpolation is disabled, the oscilloscope does not interpolate points in the waveform. If the oscilloscope cannot sample a value for a point in the waveform, the driver sets the corresponding element in the waveformArray to an IEEE-defined NaN (Not a Number) value. Check for this value with math.isnan() or numpy.isnan(). Check an entire array with </p>
<p> any(any(math.isnan(b) for b in a) for a in waveform)</p>
<dt><code>channels[].name</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.7</i> </p>
<p> This attribute returns the repeated capability identifier defined by specific driver for the channel that corresponds to the index that the user specifies. If the driver defines a qualified channel name, this property returns the qualified name. </p>
<p> If the value that the user passes for the Index parameter is less than zero or greater than the value of the channel count, the attribute raises a SelectorRangeException.</p>
<dt><code>channels[].offset</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.24</i> </p>
<p> Specifies the location of the center of the range that the Vertical Range attribute specifies. The value is with respect to ground and is in volts. </p>
<p> For example, to acquire a sine wave that spans between on 0.0 and 10.0 volts, set this attribute to 5.0 volts.</p>
<dt><code>channels[].probe_attenuation</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.16</i> </p>
<p> Specifies the scaling factor by which the probe the end-user attaches to the channel attenuates the input. For example, for a 10:1 probe, the end-user sets this attribute to 10.0. </p>
<p> Note that if the probe is changed to one with a different attenuation, and this attribute is not set, the amplitude calculations will be incorrect. </p>
<p> Querying this value will return the probe attenuation corresponding to the instrument&#8217;s actual probe attenuation. Setting this property sets Probe Attenuation Auto to False Negative values are not valid.</p>
<dt><code>channels[].range</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.25</i> </p>
<p> Specifies the absolute value of the full-scale input range for a channel. The units are volts. </p>
<p> For example, to acquire a sine wave that spans between -5.0 and 5.0 volts, set the Vertical Range attribute to 10.0 volts.</p>
<dt><code>measurement.abort</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.3.1</i> </p>
<p> This function aborts an acquisition and returns the oscilloscope to the Idle state. This function does not check the instrument status. </p>
<p> Typically, the end-user calls this function only in a sequence of calls to other low-level driver functions. The sequence performs one operation. The end-user uses the low-level functions to optimize one or more aspects of interaction with the instrument. Call the Error Query function at the conclusion of the sequence to check the instrument status. </p>
<p> If the instrument cannot abort an initiated acquisition, the driver shall return the Function Not Supported error.</p>
<dt><code>measurement.initiate</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.3.14</i> </p>
<p> This function initiates a waveform acquisition. After calling this function, the oscilloscope leaves the idle state and waits for a trigger. The oscilloscope acquires a waveform for each channel the end-user has enabled with the Configure Channel function. </p>
<p> This function does not check the instrument status. Typically, the end-user calls this function only in a sequence of calls to other low-level driver functions. The sequence performs one operation. The end-user uses the low-level functions to optimize one or more aspects of interaction with the instrument. Call the Error Query function at the conclusion of the sequence to check the instrument status.</p>
<dt><code>measurement.status</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.2</i> </p>
<p> Acquisition status indicates whether an acquisition is in progress, complete, or if the status is unknown. </p>
<p> Acquisition status is not the same as instrument status, and does not necessarily check for instrument errors. To make sure that the instrument is checked for errors after getting the acquisition status, call the Error Query method. (Note that the end user may want to call Error Query at the end of a sequence of other calls which include getting the acquisition status &#8211; it does not necessarily need to be called immediately.) </p>
<p> If the driver cannot determine whether the acquisition is complete or not, it returns the Acquisition Status Unknown value. </p>
<p> Values: * &#8216;compete&#8217; * &#8216;in_progress&#8217; * &#8216;unknown&#8217;</p>
<dt><code>trigger.configure</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.3.10</i> </p>
<p> This function configures the common attributes of the trigger subsystem. These attributes are the trigger type and trigger holdoff. </p>
<p> When the end-user calls Read Waveform, Read Waveform Measurement, Read Min Max Waveform, or Initiate Acquisition, the oscilloscope waits for a trigger. The end-user specifies the type of trigger for which the oscilloscope waits with the TriggerType parameter. </p>
<p> If the oscilloscope requires multiple waveform acquisitions to build a complete waveform, it waits for the length of time the end-user specifies with the Holdoff parameter to elapse since the previous trigger. The oscilloscope then waits for the next trigger. Once the oscilloscope acquires a complete waveform, it returns to the idle state.</p>
<dt><code>trigger.coupling</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.17</i> </p>
<p> Specifies how the oscilloscope couples the trigger source. </p>
<p> Values:</p>
<dt>&bull;</p>
<dd> &#8216;ac&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;dc&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;lf_reject&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;hf_reject&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;noise_reject&#8217;</p>
<dt><code>trigger.edge.configure</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.3.9</i> </p>
<p> This function sets the edge triggering attributes. An edge trigger occurs when the trigger signal that the end-user specifies with the Source parameter passes through the voltage threshold that the end-user specifies with the level parameter and has the slope that the end-user specifies with the Slope parameter. </p>
<p> This function affects instrument behavior only if the Trigger Type is Edge Trigger. Set the Trigger Type and Trigger Coupling before calling this function. </p>
<p> If the trigger source is one of the analog input channels, an application program should configure the vertical range, vertical offset, vertical coupling, probe attenuation, and the maximum input frequency before calling this function.</p>
<dt><code>trigger.edge.slope</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.20</i> </p>
<p> Specifies whether a rising or a falling edge triggers the oscilloscope. </p>
<p> This attribute affects instrument operation only when the Trigger Type attribute is set to Edge Trigger.</p>
<dt><code>Values:</code></p>
<dd>
<dt>&bull;</p>
<dd> &#8216;positive&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;negative&#8217;</p>
<dt><code>trigger.holdoff</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.18</i> </p>
<p> Specifies the length of time the oscilloscope waits after it detects a trigger until the oscilloscope enables the trigger subsystem to detect another trigger. The units are seconds. The Trigger Holdoff attribute affects instrument operation only when the oscilloscope requires multiple acquisitions to build a complete waveform. The oscilloscope requires multiple waveform acquisitions when it uses equivalent-time sampling or when the Acquisition Type attribute is set to Envelope or Average. </p>
<p> Note: Many scopes have a small, non-zero value as the minimum value for this attribute. To configure the instrument to use the shortest trigger hold-off, the user can specify a value of zero for this attribute. </p>
<p> Therefore, the IVI Class-Compliant specific driver shall coerce any value between zero and the minimum value to the minimum value. No other coercion is allowed on this attribute.</p>
<dt><code>trigger.level</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.19</i> </p>
<p> Specifies the voltage threshold for the trigger sub-system. The units are volts. This attribute affects instrument behavior only when the Trigger Type is set to one of the following values: Edge Trigger, Glitch Trigger, or Width Trigger. </p>
<p> This attribute, along with the Trigger Slope, Trigger Source, and Trigger Coupling attributes, defines the trigger event when the Trigger Type is set to Edge Trigger.</p>
<dt><code>trigger.source</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.21</i> </p>
<p> Specifies the source the oscilloscope monitors for the trigger event. The value can be a channel name alias, a driver-specific channel string, or one of the values below. </p>
<p> This attribute affects the instrument operation only when the Trigger Type is set to one of the following values: Edge Trigger, TV Trigger, Runt Trigger, Glitch Trigger, or Width Trigger.</p>
<dt><code>trigger.type</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeBase, section 4.2.22</i> </p>
<p> Specifies the event that triggers the oscilloscope. </p>
<p> Values:</p>
<dt>&bull;</p>
<dd> &#8216;edge&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;tv&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;runt&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;glitch&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;width&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;immediate&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;ac_line&#8217;</dl>
<h3><code>Interpolation</code> class</h3>
<dl>
<dt><code>class ivi.scope.Interpolation(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting interpolation</p>
<dt><code>acquisition.interpolation</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeInterpolation, section 5.2.1</i> </p>
<p> Specifies the interpolation method the oscilloscope uses when it cannot resolve a voltage for every point in the waveform record. </p>
<p> Values: * &#8216;none&#8217; * &#8216;sinex&#8217; * &#8216;linear&#8217;</dl>
<h3><code>TVTrigger</code> class</h3>
<dl>
<dt><code>class ivi.scope.TVTrigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting TV triggering</p>
<dt><code>trigger.tv.configure</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeTVTrigger, section 6.3.2</i> </p>
<p> This function configures the oscilloscope for TV triggering. It configures the TV signal format, the event and the signal polarity. </p>
<p> This function affects instrument behavior only if the trigger type is TV Trigger. Set the Trigger Type and Trigger Coupling before calling this function.</p>
<dt><code>trigger.tv.line_number</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeTVTrigger, section 6.2.2</i> </p>
<p> Specifies the line on which the oscilloscope triggers. The driver uses this attribute when the TV Trigger Event is set to TV Event Line Number. The line number setting is independent of the field. This means that to trigger on the first line of the second field, the user must configure the line number to the value of 263 (if we presume that field one had 262 lines).</p>
<dt><code>trigger.tv.polarity</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeTVTrigger, section 6.2.3</i> </p>
<p> Specifies the polarity of the TV signal. </p>
<p> Values: * &#8216;positive&#8217; * &#8216;negative&#8217;</p>
<dt><code>trigger.tv.signal_format</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeTVTrigger, section 6.2.4</i> </p>
<p> Specifies the format of TV signal on which the oscilloscope triggers. </p>
<p> Values: * &#8216;ntsc&#8217; * &#8216;pal&#8217; * &#8216;secam&#8217;</p>
<dt><code>trigger.tv.trigger_event</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeTVTrigger, section 6.2.1</i> </p>
<p> Specifies the event on which the oscilloscope triggers. </p>
<p> Values: * &#8216;field1&#8217; * &#8216;field2&#8217; * &#8216;any_field&#8217; * &#8216;any_line&#8217; * &#8216;line_number&#8217;</dl>
<h3><code>RuntTrigger</code> class</h3>
<dl>
<dt><code>class ivi.scope.RuntTrigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting runt triggering</p>
<dt><code>trigger.runt.configure</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeRuntTrigger, section 7.3.1</i> </p>
<p> This function configures the runt trigger. A runt trigger occurs when the trigger signal crosses one of the runt thresholds twice without crossing the other runt threshold. The end-user specifies the runt thresholds with the RuntLowThreshold and RuntHighThreshold parameters. The end-user specifies the polarity of the runt with the RuntPolarity parameter. </p>
<p> This function affects instrument behavior only if the trigger type is Runt Trigger. Set the trigger type and trigger coupling before calling this function.</p>
<dt><code>trigger.runt.polarity</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeRuntTrigger, section 7.2.3</i> </p>
<p> Specifies the polarity of the runt that triggers the oscilloscope. </p>
<p> Values: * &#8216;positive&#8217; * &#8216;negative&#8217; * &#8216;either&#8217;</p>
<dt><code>trigger.runt.threshold_high</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeRuntTrigger, section 7.2.1</i> </p>
<p> Specifies the high threshold the oscilloscope uses for runt triggering. The units are volts.</p>
<dt><code>trigger.runt.threshold_low</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeRuntTrigger, section 7.2.2</i> </p>
<p> Specifies the low threshold the oscilloscope uses for runt triggering. The units are volts.</dl>
<h3><code>GlitchTrigger</code> class</h3>
<dl>
<dt><code>class ivi.scope.GlitchTrigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting glitch triggering</p>
<dt><code>trigger.glitch.condition</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeGlitchTrigger, section 8.2.1</i> </p>
<p> Specifies the glitch condition. This attribute determines whether the glitch trigger happens when the oscilloscope detects a pulse with a width less than or greater than the width value. </p>
<p> Values: * &#8216;greater_than&#8217; * &#8216;less_than&#8217;</p>
<dt><code>trigger.glitch.configure</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeGlitchTrigger, section 8.3.1</i> </p>
<p> This function configures the glitch trigger. A glitch trigger occurs when the trigger signal has a pulse with a width that is less than or greater than the glitch width. The end user specifies which comparison criterion to use with the GlitchCondition parameter. The end-user specifies the glitch width with the GlitchWidth parameter. The end-user specifies the polarity of the pulse with the GlitchPolarity parameter. The trigger does not actually occur until the edge of a pulse that corresponds to the GlitchWidth and GlitchPolarity crosses the threshold the end-user specifies in the TriggerLevel parameter. </p>
<p> This function affects instrument behavior only if the trigger type is Glitch Trigger. Set the trigger type and trigger coupling before calling this function.</p>
<dt><code>trigger.glitch.polarity</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeGlitchTrigger, section 8.2.2</i> </p>
<p> Specifies the polarity of the glitch that triggers the oscilloscope. </p>
<p> Values: * &#8216;positive&#8217; * &#8216;negative&#8217; * &#8216;either&#8217;</p>
<dt><code>trigger.glitch.width</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeGlitchTrigger, section 8.2.3</i> </p>
<p> Specifies the glitch width. The units are seconds. The oscilloscope triggers when it detects a pulse with a width less than or greater than this value, depending on the Glitch Condition attribute.</dl>
<h3><code>WidthTrigger</code> class</h3>
<dl>
<dt><code>class ivi.scope.WidthTrigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting width triggering</p>
<dt><code>trigger.width.condition</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeWidthTrigger, section 9.2.1</i> </p>
<p> Specifies whether a pulse that is within or outside the high and low thresholds triggers the oscilloscope. The end-user specifies the high and low thresholds with the Width High Threshold and Width Low Threshold attributes. </p>
<p> Values: * &#8216;within&#8217; * &#8216;outside&#8217;</p>
<dt><code>trigger.width.configure</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeWidthTrigger, section 9.3.1</i> </p>
<p> This function configures the width trigger. A width trigger occurs when the oscilloscope detects a positive or negative pulse with a width between, or optionally outside, the width thresholds. The end-user specifies the width thresholds with the WidthLowThreshold and WidthHighThreshold parameters. The end-user specifies whether the oscilloscope triggers on pulse widths that are within or outside the width thresholds with the WidthCondition parameter. The end-user specifies the polarity of the pulse with the WidthPolarity parameter. The trigger does not actually occur until the edge of a pulse that corresponds to the WidthLowThreshold, WidthHighThreshold, WidthCondition, and WidthPolarity crosses the threshold the end-user specifies with the TriggerLevel parameter. </p>
<p> This function affects instrument behavior only if the trigger type is Width Trigger. Set the trigger type and trigger coupling before calling this function.</p>
<dt><code>trigger.width.polarity</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeWidthTrigger, section 9.2.4</i> </p>
<p> Specifies the polarity of the pulse that triggers the oscilloscope. </p>
<p> Values: * &#8216;positive&#8217; * &#8216;negative&#8217; * &#8216;either&#8217;</p>
<dt><code>trigger.width.threshold_high</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeWidthTrigger, section 9.2.2</i> </p>
<p> Specifies the high width threshold time. Units are seconds.</p>
<dt><code>trigger.width.threshold_low</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeWidthTrigger, section 9.2.3</i> </p>
<p> Specifies the low width threshold time. Units are seconds.</dl>
<h3><code>AcLineTrigger</code> class</h3>
<dl>
<dt><code>class ivi.scope.AcLineTrigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting AC line triggering</p>
<dt><code>trigger.ac_line.slope</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeAcLineTrigger, section 10.2.1</i> </p>
<p> Specifies the slope of the zero crossing upon which the scope triggers. </p>
<p> Values: * &#8216;positive&#8217; * &#8216;negative&#8217; * &#8216;either&#8217;</dl>
<h3><code>WaveformMeasurement</code> class</h3>
<dl>
<dt><code>class ivi.scope.WaveformMeasurement(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting waveform measurements</p>
<dt><code>channels[].measurement.fetch_waveform_measurement</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeWaveformMeasurement, section 11.3.2</i> </p>
<p> This function fetches a specified waveform measurement from a specific channel from a previously initiated waveform acquisition. If the channel is not enabled for the acquisition, this function returns the Channel Not Enabled error. </p>
<p> This function obtains a waveform measurement and returns the measurement value. The end-user specifies a particular measurement type, such as rise time, frequency, and voltage peak-to-peak. The waveform on which the oscilloscope calculates the waveform measurement is from an acquisition that was previously initiated. </p>
<p> Use the Initiate Acquisition function to start an acquisition on the channels that were enabled with the Configure Channel function. The oscilloscope acquires waveforms for the enabled channels concurrently. Use the Acquisition Status function to determine when the acquisition is complete. Call this function separately for each waveform measurement on a specific channel. </p>
<p> The end-user can call the Read Waveform Measurement function instead of the Initiate Acquisition function. The Read Waveform Measurement function starts an acquisition on all enabled channels. It then waits for the acquisition to complete, obtains a waveform measurement on the specified channel, and returns the measurement value. Call this function separately to obtain any other waveform measurements on a specific channel. </p>
<p> Configure the appropriate reference levels before calling this function to take a rise time, fall time, width negative, width positive, duty cycle negative, or duty cycle positive measurement. </p>
<p> The end-user can configure the low, mid, and high references either by calling the Configure Reference Levels function or by setting the following attributes.</p>
<dt>&bull;</p>
<dd> Measurement High Reference</p>
<dt>&bull;</p>
<dd> Measurement Low Reference</p>
<dt>&bull;</p>
<dd> Measurement Mid Reference </p>
<p> This function does not check the instrument status. Typically, the end-user calls this function only in a sequence of calls to other low-level driver functions. The sequence performs one operation. The end-user uses the low-level functions to optimize one or more aspects of interaction with the instrument. Call the Error Query function at the conclusion of the sequence to check the instrument status. </p>
<p> Values for measurement_function: * &#8216;rise_time&#8217; * &#8216;fall_time&#8217; * &#8216;frequency&#8217; * &#8216;period&#8217; * &#8216;voltage_rms&#8217; * &#8216;voltage_peak_to_peak&#8217; * &#8216;voltage_max&#8217; * &#8216;voltage_min&#8217; * &#8216;voltage_high&#8217; * &#8216;voltage_low&#8217; * &#8216;voltage_average&#8217; * &#8216;width_negative&#8217; * &#8216;width_positive&#8217; * &#8216;duty_cycle_negative&#8217; * &#8216;duty_cycle_positive&#8217; * &#8216;amplitude&#8217; * &#8216;voltage_cycle_rms&#8217; * &#8216;voltage_cycle_average&#8217; * &#8216;overshoot&#8217; * &#8216;preshoot&#8217;</p>
<dt><code>channels[].measurement.read_waveform_measurement</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeWaveformMeasurement, section 11.3.3</i> </p>
<p> This function initiates a new waveform acquisition and returns a specified waveform measurement from a specific channel. </p>
<p> This function initiates an acquisition on the channels that the end-user enables with the Configure Channel function. If the channel is not enabled for the acquisition, this function returns Channel Not Enabled error. It then waits for the acquisition to complete, obtains a waveform measurement on the channel the end-user specifies, and returns the measurement value. The end-user specifies a particular measurement type, such as rise time, frequency, and voltage peak-to-peak. </p>
<p> If the oscilloscope did not complete the acquisition within the time period the user specified with the MaxTimeMilliseconds parameter, the function returns the Max Time Exceeded error. </p>
<p> The end-user can call the Fetch Waveform Measurement function separately to obtain any other waveform measurement on a specific channel without initiating another acquisition. </p>
<p> The end-user must configure the appropriate reference levels before calling this function. Configure the low, mid, and high references either by calling the Configure Reference Levels function or by setting the following attributes. following attributes.</p>
<dt>&bull;</p>
<dd> Measurement High Reference</p>
<dt>&bull;</p>
<dd> Measurement Low Reference</p>
<dt>&bull;</p>
<dd> Measurement Mid Reference</p>
<dt><code>reference_level.configure</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeWaveformMeasurement, section 11.3.1</i> </p>
<p> This function configures the reference levels for waveform measurements. Call this function before calling the Read Waveform Measurement or Fetch Waveform Measurement to take waveform measurements.</p>
<dt><code>reference_level.high</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeWaveformMeasurement, section 11.2.1</i> </p>
<p> Specifies the high reference the oscilloscope uses for waveform measurements. The value is a percentage of the difference between the Voltage High and Voltage Low.</p>
<dt><code>reference_level.low</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeWaveformMeasurement, section 11.2.2</i> </p>
<p> Specifies the low reference the oscilloscope uses for waveform measurements. The value is a percentage of the difference between the Voltage High and Voltage Low.</p>
<dt><code>reference_level.middle</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeWaveformMeasurement, section 11.2.3</i> </p>
<p> Specifies the middle reference the oscilloscope uses for waveform measurements. The value is a percentage of the difference between the Voltage High and Voltage Low.</dl>
<h3><code>MinMaxWaveform</code> class</h3>
<dl>
<dt><code>class ivi.scope.MinMaxWaveform(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting minimum and maximum waveform acquisition</p>
<dt><code>acquisition.number_of_envelopes</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeMinMaxWaveform, section 12.2.1</i> </p>
<p> When the end-user sets the Acquisition Type attribute to Envelope, the oscilloscope acquires multiple waveforms. After each waveform acquisition, the oscilloscope keeps the minimum and maximum values it finds for each point in the waveform record. This attribute specifies the number of waveforms the oscilloscope acquires and analyzes to create the minimum and maximum waveforms. After the oscilloscope acquires as many waveforms as this attribute specifies, it returns to the idle state. This attribute affects instrument operation only when the Acquisition Type attribute is set to Envelope.</p>
<dt><code>channels[].measurement.fetch_waveform_min_max</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeMinMaxWaveform, section 12.3.2</i> </p>
<p> This function returns the minimum and maximum waveforms that the oscilloscope acquires for the specified channel. If the channel is not enabled for the acquisition, this function returns the Channel Not Enabled error. </p>
<p> The waveforms are from a previously initiated acquisition. Use this function to fetch waveforms when the acquisition type is set to Peak Detect or Envelope. If the acquisition type is not one of the listed types, the function returns the Invalid Acquisition Type error. </p>
<p> Use the Initiate Acquisition function to start an acquisition on the enabled channels. The oscilloscope acquires the min/max waveforms for the enabled channels concurrently. Use the Acquisition Status function to determine when the acquisition is complete. The end-user must call this function separately for each enabled channel to obtain the min/max waveforms. </p>
<p> The end-user can call the Read Min Max Waveform function instead of the Initiate Acquisition function. The Read Min Max Waveform function starts an acquisition on all enabled channels, waits for the acquisition to complete, and returns the min/max waveforms for the specified channel. You call this function to obtain the min/max waveforms for each of the remaining channels. </p>
<p> After this function executes, each element in the MinWaveform and MaxWaveform parameters is either a voltage or a value indicating that the oscilloscope could not sample a voltage. </p>
<p> The return value is a list of (x, y_min, y_max) tuples that represent the time and voltage of each data point. Either of the y points may be NaN in the case that the oscilloscope could not sample the voltage. </p>
<p> The end-user configures the interpolation method the oscilloscope uses with the Acquisition.Interpolation property. If interpolation is disabled, the oscilloscope does not interpolate points in the waveform. If the oscilloscope cannot sample a value for a point in the waveform, the driver sets the corresponding element in the waveformArray to an IEEE-defined NaN (Not a Number) value. Check for this value with math.isnan() or numpy.isnan(). Check an entire array with </p>
<p> any(any(math.isnan(b) for b in a) for a in waveform) </p>
<p> This function does not check the instrument status. Typically, the end-user calls this function only in a sequence of calls to other low-level driver functions. The sequence performs one operation. The end-user uses the low-level functions to optimize one or more aspects of interaction with the instrument. Call the Error Query function at the conclusion of the sequence to check the instrument status.</p>
<dt><code>channels[].measurement.read_waveform_min_max</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeMinMaxWaveform, section 12.3.3</i> </p>
<p> This function initiates new waveform acquisition and returns minimum and maximum waveforms from a specific channel. If the channel is not enabled for the acquisition, this function returns the Channel Not Enabled error. </p>
<p> This function is used when the Acquisition Type is Peak Detect or Envelope. If the acquisition type is not one of the listed types, the function returns the Invalid Acquisition Type error. </p>
<p> This function initiates an acquisition on the enabled channels. It then waits for the acquisition to complete, and returns the min/max waveforms for the specified channel. Call the Fetch Min Max Waveform function to obtain the min/max waveforms for each of the remaining enabled channels without initiating another acquisition. If the oscilloscope did not complete the acquisition within the time period the user specified with the max_time parameter, the function returns the Max Time Exceeded error. </p>
<p> The return value is a list of (x, y_min, y_max) tuples that represent the time and voltage of each data point. Either of the y points may be NaN in the case that the oscilloscope could not sample the voltage. </p>
<p> The end-user configures the interpolation method the oscilloscope uses with the Acquisition.Interpolation property. If interpolation is disabled, the oscilloscope does not interpolate points in the waveform. If the oscilloscope cannot sample a value for a point in the waveform, the driver sets the corresponding element in the waveformArray to an IEEE-defined NaN (Not a Number) value. Check for this value with math.isnan() or numpy.isnan(). Check an entire array with </p>
<p> any(any(math.isnan(b) for b in a) for a in waveform) </p>
<p> This function does not check the instrument status. Typically, the end-user calls this function only in a sequence of calls to other low-level driver functions. The sequence performs one operation. The end-user uses the low-level functions to optimize one or more aspects of interaction with the instrument. Call the Error Query function at the conclusion of the sequence to check the instrument status.</dl>
<h3><code>ProbeAutoSense</code> class</h3>
<dl>
<dt><code>class ivi.scope.ProbeAutoSense(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting probe attenuation sensing</p>
<dt><code>channels[].probe_attenuation_auto</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeProbeAutoSense, section 13.2.1</i> </p>
<p> If this attribute is True, the driver configures the oscilloscope to sense the attenuation of the probe automatically. </p>
<p> If this attribute is False, the driver disables the automatic probe sense and configures the oscilloscope to use the value of the Probe Attenuation attribute. </p>
<p> The actual probe attenuation the oscilloscope is currently using can be determined from the Probe Attenuation attribute. </p>
<p> Setting the Probe Attenuation attribute also sets the Probe Attenuation Auto attribute to false.</dl>
<h3><code>ContinuousAcquisition</code> class</h3>
<dl>
<dt><code>class ivi.scope.ContinuousAcquisition(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting continuous acquisition</p>
<dt><code>trigger.continuous</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeContinuousAcquisition, section 14.2.1</i> </p>
<p> Specifies whether the oscilloscope continuously initiates waveform acquisition. If the end-user sets this attribute to True, the oscilloscope immediately waits for another trigger after the previous waveform acquisition is complete. Setting this attribute to True is useful when the end-user requires continuous updates of the oscilloscope display. This specification does not define the behavior of the read waveform and fetch waveform functions when this attribute is set to True. The behavior of these functions is instrument specific.</dl>
<h3><code>AverageAcquisition</code> class</h3>
<dl>
<dt><code>class ivi.scope.AverageAcquisition(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting average acquisition</p>
<dt><code>acquisition.number_of_averages</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeAverageAcquisition, section 15.2.1</i> </p>
<p> Specifies the number of waveform the oscilloscope acquires and averages. After the oscilloscope acquires as many waveforms as this attribute specifies, it returns to the idle state. This attribute affects instrument behavior only when the Acquisition Type attribute is set to Average.</dl>
<h3><code>SampleMode</code> class</h3>
<dl>
<dt><code>class ivi.scope.SampleMode(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting equivalent and real time acquisition</p>
<dt><code>acquisition.sample_mode</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeSampleMode, section 16.2.1</i> </p>
<p> Returns the sample mode the oscilloscope is currently using. </p>
<p> Values: * &#8216;real_time&#8217; * &#8216;equivalent_time&#8217;</dl>
<h3><code>TriggerModifier</code> class</h3>
<dl>
<dt><code>class ivi.scope.TriggerModifier(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting specific triggering subsystem behavior in the absence of a trigger</p>
<dt><code>trigger.modifier</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeTriggerModifier, section 17.2.1</i> </p>
<p> Specifies the trigger modifier. The trigger modifier determines the oscilloscope&#8217;s behavior in the absence of the configured trigger. </p>
<p> Values: * &#8216;none&#8217; * &#8216;auto&#8217; * &#8216;auto_level&#8217;</dl>
<h3><code>AutoSetup</code> class</h3>
<dl>
<dt><code>class ivi.scope.AutoSetup(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for oscilloscopes supporting automatic setup</p>
<dt><code>measurement.auto_setup</code></p>
<dd> <i>IVI class IviScope, capability group IviScopeAutoSetup, section 18.2.1</i> </p>
<p> This function performs an auto-setup on the instrument.</dl>
<h2>IVI.FGEN &#8212; FUNCTION GENERATOR CLASS</h2>
<p> This module provides the base functionality for Function Generators.</p>
<h3>Functions and Exceptions</h3>
<dl>
<dt><code>exception ivi.fgen.IviException</code></p>
<dd> Exception raised on various occasions; argument is a string describing what is wrong.</dl>
<h3><code>Base</code> class</h3>
<dl>
<dt><code>class ivi.fgen.Base(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Base IVI methods for all function generators</p>
<dt><code>ivi.fgen.abort_generation</code></p>
<dd> Aborts a previously initiated signal generation. If the function generator is in the Output Generation State, this function moves the function generator to the Configuration State. If the function generator is already in the Configuration State, the function does nothing and returns Success. </p>
<p> This specification requires that the user be able to configure the output of the function generator regardless of whether the function generator is in the Configuration State or the Generation State. This means that the user is not required to call Abort Generation prior to configuring the output of the function generator. </p>
<p> Many function generators constantly generate an output signal, and do not require the user to abort signal generation prior to configuring the instrument. If a function generator&#8217;s output cannot be aborted (i.e., the function generator cannot stop generating a signal) this function does nothing and returns Success. </p>
<p> Some function generators require that the user abort signal generation prior to configuring the instrument. The specific drivers for these types of instruments must compensate for this restriction and allow the user to configure the instrument without requiring the user to call Abort Generation. For these types of instruments, there is often a significant performance increase if the user configures the output while the instrument is not generating a signal. </p>
<p> The user is not required to call Abort Generation or Initiate Generation. Whether the user chooses to call these functions in an application program has no impact on interchangeability. The user can choose to use these functions if they want to optimize their application for instruments that exhibit increased performance when output configuration is performed while the instrument is not generating a signal.</p>
<dt><code>ivi.fgen.initiate_generation</code></p>
<dd> Initiates signal generation. If the function generator is in the Configuration State, this function moves the function generator to the Output Generation State. If the function generator is already in the Output Generation State, this function does nothing and returns Success. </p>
<p> This specification requires that the instrument be in the Generation State after the user calls the Initialize or Reset functions. This specification also requires that the user be able to configure the output of the function generator regardless of whether the function generator is in the Configuration State or the Generation State. This means that the user is only required to call Initiate Generation if they abort signal generation by calling Abort Generation. </p>
<p> Many function generators constantly generate an output signal, and do not require the user to abort signal generation prior to configuring the instrument. If a function generator&#8217;s output cannot be aborted (i.e., the function generator cannot stop generating a signal) this function does nothing and returns Success. </p>
<p> Some function generators require that the user abort signal generation prior to configuring the instrument. The specific drivers for these types of instruments must compensate for this restriction and allow the user to configure the instrument without requiring the user to call Abort Generation. For these types of instruments, there is often a significant performance increase if the user configures the output while the instrument is not generating a signal. </p>
<p> The user is not required to call Abort Generation or Initiate Generation. Whether the user chooses to call these functions in an application program has no impact on interchangeability. The user can choose to use these functions if they want to optimize their application for instruments that exhibit increased performance when output configuration is performed while the instrument is not generating a signal.</p>
<dt><code>outputs.enabled</code></p>
<dd> If set to True, the signal the function generator produces appears at the output connector. If set to False, the signal the function generator produces does not appear at the output connector.</p>
<dt><code>outputs.impedance</code></p>
<dd> Specifies the impedance of the output channel. The units are Ohms.</p>
<dt><code>outputs.name</code></p>
<dd> This property returns the physical name defined by the specific driver for the output channel that corresponds to the 0-based index that the user specifies. If the driver defines a qualified channel name, this property returns the qualified name. If the value that the user passes for the Index parameter is less than zero or greater than the value of Output Count, the property returns an empty string and returns an error.</p>
<dt><code>outputs.operation_mode</code></p>
<dd> Specifies how the function generator produces output on a channel. </p>
<p> Values for operation_mode:</p>
<dt>&bull;</p>
<dd> &#8216;continuous&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;burst&#8217;</p>
<dt><code>outputs.output_mode</code></p>
<dd> Determines how the function generator produces waveforms. This attribute determines which extension group&#8217;s functions and attributes are used to configure the waveform the function generator produces. </p>
<p> Values for output_mode:</p>
<dt>&bull;</p>
<dd> &#8216;function&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;arbitrary&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;sequence&#8217;</p>
<dt><code>outputs.reference_clock_source</code></p>
<dd> Specifies the source of the reference clock. The function generator derives frequencies and sample rates that it uses to generate waveforms from the reference clock. </p>
<p> The source of the reference clock is a string. If an IVI driver supports a reference clock source and the reference clock source is listed in IVI-3.3 Cross Class Capabilities Specification, Section 3, then the IVI driver shall accept the standard string for that reference clock. This attribute is case insensitive, but case preserving. That is, the setting is case insensitive but when reading it back the programmed case is returned. IVI specific drivers may define new reference clock source strings for reference clock sources that are not defined by IVI-3.3 Cross Class Capabilities Specification if needed.</dl>
<h3><code>StdFunc</code> class</h3>
<dl>
<dt><code>class ivi.fgen.StdFunc(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that can produce manufacturer-supplied periodic waveforms</p>
<dt><code>outputs.standard_waveform.amplitude</code></p>
<dd> Specifies the amplitude of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output. The units are volts.</p>
<dt><code>outputs.standard_waveform.configure</code></p>
<dd> This function configures the attributes of the function generator that affect standard waveform generation. These attributes are the Waveform, Amplitude, DC Offset, Frequency, and Start Phase. </p>
<p> When the Waveform parameter is set to Waveform DC, this function ignores the Amplitude, Frequency, and Start Phase parameters and does not set the Amplitude, Frequency, and Start Phase attributes.</p>
<dt><code>outputs.standard_waveform.dc_offset</code></p>
<dd> Specifies the DC offset of the standard waveform the function generator produces. If the Waveform attribute is set to Waveform DC, this attribute specifies the DC level the function generator produces. The units are volts.</p>
<dt><code>outputs.standard_waveform.duty_cycle_high</code></p>
<dd> Specifies the duty cycle for a square waveform. This attribute affects function generator behavior only when the Waveform attribute is set to Waveform Square. The value is expressed as a percentage.</p>
<dt><code>outputs.standard_waveform.frequency</code></p>
<dd> Specifies the frequency of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output. The units are Hertz.</p>
<dt><code>outputs.standard_waveform.start_phase</code></p>
<dd> Specifies the start phase of the standard waveform the function generator produces. When the Waveform attribute is set to Waveform DC, this attribute does not affect signal output. The units are degrees.</p>
<dt><code>outputs.standard_waveform.waveform</code></p>
<dd> Specifies which standard waveform the function generator produces. </p>
<p> Values for waveform:</p>
<dt>&bull;</p>
<dd> &#8216;sine&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;square&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;triangle&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;ramp_up&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;ramp_down&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;dc&#8217;</dl>
<h3><code>ArbWfm</code> class</h3>
<dl>
<dt><code>class ivi.fgen.ArbWfm(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that can produce arbitrary waveforms</p>
<dt><code>arbitrary.sample_rate</code></p>
<dd> Specifies the sample rate of the arbitrary waveforms the function generator produces. The units are samples per second.</p>
<dt><code>arbitrary.waveform.clear</code></p>
<dd> Removes a previously created arbitrary waveform from the function generator&#8217;s memory and invalidates the waveform&#8217;s handle. </p>
<p> If the waveform cannot be cleared because it is currently being generated, or it is specified as part of an existing arbitrary waveform sequence, this function returns the Waveform In Use error.</p>
<dt><code>arbitrary.waveform.configure</code></p>
<dd> Configures the attributes of the function generator that affect arbitrary waveform generation. These attributes are the arbitrary waveform handle, gain, and offset.</p>
<dt><code>arbitrary.waveform.create</code></p>
<dd> Creates an arbitrary waveform from an array of data points. The function returns a handlethat identifies the waveform. You pass a waveform handle to the Handle parameter of the Configure Arbitrary Waveform function to produce that waveform.</p>
<dt><code>arbitrary.waveform.number_waveforms_max</code></p>
<dd> Returns the maximum number of arbitrary waveforms that the function generator allows.</p>
<dt><code>arbitrary.waveform.quantum</code></p>
<dd> The size of each arbitrary waveform shall be a multiple of a quantum value. This attribute returns the quantum value the function generator allows. For example, if this attribute returns a value of 8, all waveform sizes must be a multiple of 8.</p>
<dt><code>arbitrary.waveform.size_max</code></p>
<dd> Returns the maximum number of points the function generator allows in an arbitrary waveform.</p>
<dt><code>arbitrary.waveform.size_min</code></p>
<dd> Returns the minimum number of points the function generator allows in an arbitrary waveform.</p>
<dt><code>outputs.arbitrary.configure</code></p>
<dd> Configures the attributes of the function generator that affect arbitrary waveform generation. These attributes are the arbitrary waveform handle, gain, and offset.</p>
<dt><code>outputs.arbitrary.gain</code></p>
<dd> Specifies the gain of the arbitrary waveform the function generator produces. This value is unitless.</p>
<dt><code>outputs.arbitrary.offset</code></p>
<dd> Specifies the offset of the arbitrary waveform the function generator produces. The units are volts.</p>
<dt><code>outputs.arbitrary.waveform</code></p>
<dd></dl>
<h3><code>ArbChannelWfm</code> class</h3>
<dl>
<dt><code>class ivi.fgen.ArbChannelWfm(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support user-defined arbitrary waveform generation</p>
<dt><code>arbitrary.waveform.create_channel_waveform</code></p>
<dd> Creates a channel-specific arbitrary waveform and returns a handle that identifies that waveform. You pass a waveform handle as the waveformHandle parameter of the Configure Arbitrary Waveform function to produce that waveform. You also use the handles this function returns to create a sequence of arbitrary waveforms with the Create Arbitrary Sequence function. </p>
<p> If the instrument has multiple channels, it is possible to create multi-channel waveforms: the channel names are passed as a comma-separated list of channel names, and the waveform arrays are concatenated into a single array. In this case, all waveforms must be of the same length. </p>
<p> If the function generator cannot store any more arbitrary waveforms, this function returns the error No Waveforms Available.</p>
<dt><code>outputs.arbitrary.create_waveform</code></p>
<dd> Creates a channel-specific arbitrary waveform and returns a handle that identifies that waveform. You pass a waveform handle as the waveformHandle parameter of the Configure Arbitrary Waveform function to produce that waveform. You also use the handles this function returns to create a sequence of arbitrary waveforms with the Create Arbitrary Sequence function. </p>
<p> If the instrument has multiple channels, it is possible to create multi-channel waveforms: the channel names are passed as a comma-separated list of channel names, and the waveform arrays are concatenated into a single array. In this case, all waveforms must be of the same length. </p>
<p> If the function generator cannot store any more arbitrary waveforms, this function returns the error No Waveforms Available.</dl>
<h3><code>ArbWfmBinary</code> class</h3>
<dl>
<dt><code>class ivi.fgen.ArbWfmBinary(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support user-defined arbitrary binary waveform generation</p>
<dt><code>arbitrary.binary_alignment</code></p>
<dd> Identifies whether the arbitrary waveform generator treats binary data provided to the Create Channel Arbitrary Waveform Int16 or Create Channel Arbitrary Waveform Int32 functions as left-justified or right-justified. Binary Alignment is only relevant if the generator supports bit-depths less than the size of the binarydata type of the create waveform function being used. For a 16-bit or a 32-bit generator, this function can return either value.</p>
<dt><code>arbitrary.sample_bit_resolution</code></p>
<dd> Returns the number of significant bits that the generator supports in an arbitrary waveform. Together with the binary alignment, this allows the user to know the range and resolution of the integers in the waveform.</p>
<dt><code>arbitrary.waveform.create_channel_waveform_int16</code></p>
<dd> Creates a channel-specific arbitrary waveform and returns a handle that identifies that waveform. Data is passed in as 16-bit binary data. If the arbitrary waveform generator supports formats less than 16 bits, call the BinaryAlignment property to determine whether to left or right justify the data before passing it to this call. You pass a waveform handle as the waveformHandle parameter of the Configure Arbitrary Waveform function to produce that waveform. You also use the handles this function returns to create a sequence of arbitrary waveforms with the Create Arbitrary Sequence function. </p>
<p> If the instrument has multiple channels, it is possible to create multi-channel waveforms: the channel names are passed as a comma-separated list of channel names, and the waveform arrays are concatenated into a single array. In this case, all waveforms must be of the same length. </p>
<p> If the function generator cannot store any more arbitrary waveforms, this function returns the error No Waveforms Available.</p>
<dt><code>arbitrary.waveform.create_channel_waveform_int32</code></p>
<dd> Creates a channel-specific arbitrary waveform and returns a handle that identifies that waveform. Data is passed in as 32-bit binary data. If the arbitrary waveform generator supports formats less than 32 bits, call the BinaryAlignment property to determine whether to left or right justify the data before passing it to this call. You pass a waveform handle as the waveformHandle parameter of the Configure Arbitrary Waveform function to produce that waveform. You also use the handles this function returns to create a sequence of arbitrary waveforms with the Create Arbitrary Sequence function. </p>
<p> If the instrument has multiple channels, it is possible to create multi-channel waveforms: the channel names are passed as a comma-separated list of channel names, and the waveform arrays are concatenated into a single array. In this case, all waveforms must be of the same length. </p>
<p> If the function generator cannot store any more arbitrary waveforms, this function returns the error No Waveforms Available.</p>
<dt><code>outputs.arbitrary.waveform.create_channel_waveform_int16</code></p>
<dd> Creates a channel-specific arbitrary waveform and returns a handle that identifies that waveform. Data is passed in as 16-bit binary data. If the arbitrary waveform generator supports formats less than 16 bits, call the BinaryAlignment property to determine whether to left or right justify the data before passing it to this call. You pass a waveform handle as the waveformHandle parameter of the Configure Arbitrary Waveform function to produce that waveform. You also use the handles this function returns to create a sequence of arbitrary waveforms with the Create Arbitrary Sequence function. </p>
<p> If the instrument has multiple channels, it is possible to create multi-channel waveforms: the channel names are passed as a comma-separated list of channel names, and the waveform arrays are concatenated into a single array. In this case, all waveforms must be of the same length. </p>
<p> If the function generator cannot store any more arbitrary waveforms, this function returns the error No Waveforms Available.</p>
<dt><code>outputs.arbitrary.waveform.create_channel_waveform_int32</code></p>
<dd> Creates a channel-specific arbitrary waveform and returns a handle that identifies that waveform. Data is passed in as 32-bit binary data. If the arbitrary waveform generator supports formats less than 32 bits, call the BinaryAlignment property to determine whether to left or right justify the data before passing it to this call. You pass a waveform handle as the waveformHandle parameter of the Configure Arbitrary Waveform function to produce that waveform. You also use the handles this function returns to create a sequence of arbitrary waveforms with the Create Arbitrary Sequence function. </p>
<p> If the instrument has multiple channels, it is possible to create multi-channel waveforms: the channel names are passed as a comma-separated list of channel names, and the waveform arrays are concatenated into a single array. In this case, all waveforms must be of the same length. </p>
<p> If the function generator cannot store any more arbitrary waveforms, this function returns the error No Waveforms Available.</dl>
<h3><code>DataMarker</code> class</h3>
<dl>
<dt><code>class ivi.fgen.DataMarker(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support output of particular waveform data bits as markers</p>
<dt><code>data_markers.amplitude</code></p>
<dd> Specifies the amplitude of the data marker output. The units are volts.</p>
<dt><code>data_markers.bit_position</code></p>
<dd> Specifies the bit position of the binary representation of the waveform data that will be output as a data marker. A value of 0 indicates the least significant bit.</p>
<dt><code>data_markers.clear</code></p>
<dd> Disables all of the data markers by setting their Data Marker Destination attribute to None.</p>
<dt><code>data_markers.configure</code></p>
<dd> Configures some of the common data marker attributes.</p>
<dt><code>data_markers.delay</code></p>
<dd> Specifies the amount of delay applied to the data marker output with respect to the analog data output. A value of zero indicates the marker is aligned with the analog data output. The units are seconds.</p>
<dt><code>data_markers.destination</code></p>
<dd> Specifies the destination terminal for the data marker output.</p>
<dt><code>data_markers.name</code></p>
<dd> This attribute returns the repeated capability identifier defined by specific driver for the data marker that corresponds to the index that the user specifies. If the driver defines a qualified Data Marker name, this property returns the qualified name. </p>
<p> If the value that the user passes for the Index parameter is less than zero or greater than the value of the Data Marker Count, the attribute returns an empty string for the value and returns an error.</p>
<dt><code>data_markers.polarity</code></p>
<dd> Specifies the polarity of the data marker output. </p>
<p> Values for polarity:</p>
<dt>&bull;</p>
<dd> &#8216;active_high&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;active_low&#8217;</p>
<dt><code>data_markers.source_channel</code></p>
<dd> Specifies the channel whose data bit will be output as a marker.</dl>
<h3><code>SparseMarker</code> class</h3>
<dl>
<dt><code>class ivi.fgen.SparseMarker(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support output of markers associated with output data samples</p>
<dt><code>sparse_markers.amplitude</code></p>
<dd> Specifies the amplitude of the sparse marker output. The units are volts.</p>
<dt><code>sparse_markers.clear</code></p>
<dd> Disables all of the sparse markers by setting their Sparse Marker Destination attribute to None.</p>
<dt><code>sparse_markers.configure</code></p>
<dd> Configures some of the common sparse marker attributes.</p>
<dt><code>sparse_markers.delay</code></p>
<dd> Specifies the amount of delay applied to the sparse marker output with respect to the analog data output. A value of zero indicates the marker is aligned with the analog data output. The units are seconds.</p>
<dt><code>sparse_markers.destination</code></p>
<dd> Specifies the destination terminal for the sparse marker output.</p>
<dt><code>sparse_markers.get_indexes</code></p>
<dd> Gets the coerced indexes associated with the sparse marker. These indexes are specified by either the Configure SparseMarker function or the Set Sparse Marker Indexes function.</p>
<dt><code>sparse_markers.name</code></p>
<dd> This attribute returns the repeated capability identifier defined by specific driver for the sparse marker that corresponds to the index that the user specifies. If the driver defines a qualified Sparse Marker name, this property returns the qualified name. </p>
<p> If the value that the user passes for the Index parameter is less than one or greater than the value of the Sparse Marker Count, the attribute returns an empty string for the value and returns an error.</p>
<dt><code>sparse_markers.polarity</code></p>
<dd> Specifies the polarity of the sparse marker output. </p>
<p> Values for polarity:</p>
<dt>&bull;</p>
<dd> &#8216;active_high&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;active_low&#8217;</p>
<dt><code>sparse_markers.set_indexes</code></p>
<dd> Sets the indexes associated with the sparse marker. These indexes may be coerced by the driver. Use the Get Sparse Marker Indexes function to find the coerced values.</p>
<dt><code>sparse_markers.waveform_handle</code></p>
<dd> Specifies the waveform whose indexes the sparse marker refers to.</dl>
<h3><code>ArbDataMask</code> class</h3>
<dl>
<dt><code>class ivi.fgen.ArbDataMask(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support masking of waveform data bits</p>
<dt><code>arbitrary.data_mask</code></p>
<dd> Determines which bits of the output data are masked out. This is especially useful when combined with Data Markers so that the bits embedded with the data to be used for markers are not actually output by the generator. </p>
<p> A value of 1 for a particular bit indicates that the data bit should be output. A value of 0 indicates that the data bit should be masked out. For example, if the value of this property is 0xFFFFFFFF (all bits are 1), no masking is applied.</dl>
<h3><code>ArbFrequency</code> class</h3>
<dl>
<dt><code>class ivi.fgen.ArbFrequency(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that can produce arbitrary waveforms with variable rate</p>
<dt><code>outputs.arbitrary.frequency</code></p>
<dd> Specifies the rate in Hertz at which an entire arbitrary waveform is generated.</dl>
<h3><code>ArbSeq</code> class</h3>
<dl>
<dt><code>class ivi.fgen.ArbSeq(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that can produce sequences of arbitrary waveforms</p>
<dt><code>arbitrary.clear_memory</code></p>
<dd> Removes all previously created arbitrary waveforms and sequences from the function generator&#8217;s memory and invalidates all waveform and sequence handles. </p>
<p> If a waveform cannot be cleared because it is currently being generated, this function returns the error Waveform In Use. </p>
<p> If a sequence cannot be cleared because it is currently being generated, this function returns the error Sequence In Use.</p>
<dt><code>arbitrary.sequence.clear</code></p>
<dd> Removes a previously created arbitrary sequence from the function generator&#8217;s memory and invalidates the sequence&#8217;s handle. </p>
<p> If the sequence cannot be cleared because it is currently being generated, this function returns the error Sequence In Use.</p>
<dt><code>arbitrary.sequence.configure</code></p>
<dd> Configures the attributes of the function generator that affect arbitrary sequence generation. These attributes are the arbitrary sequence handle, gain, and offset.</p>
<dt><code>arbitrary.sequence.create</code></p>
<dd> Creates an arbitrary waveform sequence from an array of waveform handles and a corresponding array of loop counts. The function returns a handle that identifies the sequence. You pass a sequence handle to the Handle parameter of the Configure Arbitrary Sequence function to produce that sequence. </p>
<p> If the function generator cannot store any more arbitrary sequences, this function returns the error No Sequences Available.</p>
<dt><code>arbitrary.sequence.length_max</code></p>
<dd> Returns the maximum number of arbitrary waveforms that the function generator allows in an arbitrary sequence.</p>
<dt><code>arbitrary.sequence.length_min</code></p>
<dd> Returns the minimum number of arbitrary waveforms that the function generator allows in an arbitrary sequence.</p>
<dt><code>arbitrary.sequence.loop_count_max</code></p>
<dd> Returns the maximum number of times that the function generator can repeat a waveform in a sequence.</p>
<dt><code>arbitrary.sequence.number_sequences_max</code></p>
<dd> Returns the maximum number of arbitrary sequences that the function generator allows.</p>
<dt><code>outputs.arbitrary.sequence.configure</code></p>
<dd> Configures the attributes of the function generator that affect arbitrary sequence generation. These attributes are the arbitrary sequence handle, gain, and offset.</dl>
<h3><code>ArbSeqDepth</code> class</h3>
<dl>
<dt><code>class ivi.fgen.ArbSeqDepth(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support producing sequences of sequences of waveforms</p>
<dt><code>arbitrary.sequence.depth_max</code></p>
<dd> Returns the maximum sequence depth &#8211; that is, the number of times a sequence can include other sequences recursively. A depth of zero indicates the generator supports waveforms only. A depth of 1 indicates a generator supports sequences of waveforms, but not sequences of sequences. A depth of 2 or greater indicates that the generator supports sequences of sequences. Note that if the MaxSequenceDepth is 2 or greater, the driver must return unique handles for waveforms and sequences so that a sequence may contain both waveform and sequence handles.</dl>
<h3><code>Trigger</code> class</h3>
<dl>
<dt><code>class ivi.fgen.Trigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support triggering</p>
<dt><code>outputs.trigger.source</code></p>
<dd> Specifies the trigger source. After the function generator receives a trigger from this source, it produces a signal.</dl>
<h3><code>InternalTrigger</code> class</h3>
<dl>
<dt><code>class ivi.fgen.InternalTrigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support internal triggering</p>
<dt><code>trigger.internal_rate</code></p>
<dd> Specifies the rate at which the function generator&#8217;s internal trigger source produces a trigger, in triggers per second.</dl>
<h3><code>SoftwareTrigger</code> class</h3>
<dl>
<dt><code>class ivi.fgen.SoftwareTrigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support software triggering</p>
<dt><code>ivi.fgen.send_software_trigger</code></p>
<dd> This function sends a software-generated trigger to the instrument. It is only applicable for instruments using interfaces or protocols which support an explicit trigger function. For example, with GPIB this function could send a group execute trigger to the instrument. Other implementations might send a <code>*TRG</code> command. </p>
<p> Since instruments interpret a software-generated trigger in a wide variety of ways, the precise response of the instrument to this trigger is not defined. Note that SCPI details a possible implementation. </p>
<p> This function should not use resources which are potentially shared by other devices (for example, the VXI trigger lines). Use of such shared resources may have undesirable effects on other devices. </p>
<p> This function should not check the instrument status. Typically, the end-user calls this function only in a sequence of calls to other low-level driver functions. The sequence performs one operation. The end-user uses the low-level functions to optimize one or more aspects of interaction with the instrument. To check the instrument status, call the appropriate error query function at the conclusion of the sequence. </p>
<p> The trigger source attribute must accept Software Trigger as a valid setting for this function to work. If the trigger source is not set to Software Trigger, this function does nothing and returns the error Trigger Not Software.</dl>
<h3><code>Burst</code> class</h3>
<dl>
<dt><code>class ivi.fgen.Burst(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support triggered burst output</p>
<dt><code>outputs.burst_count</code></p>
<dd> Specifies the number of waveform cycles that the function generator produces after it receives a trigger.</dl>
<h3><code>ModulateAM</code> class</h3>
<dl>
<dt><code>class ivi.fgen.ModulateAM(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support amplitude modulation</p>
<dt><code>am.configure_internal</code></p>
<dd> Configures the attributes that control the function generator&#8217;s internal amplitude modulating waveform source. These attributes are the modulation depth, waveform, and frequency.</p>
<dt><code>am.internal_depth</code></p>
<dd> Specifies the extent of modulation the function generator applies to the carrier waveform when the AM Source attribute is set to AM Internal. The unit is percentage. </p>
<p> This attribute affects the behavior of the instrument only when the AM ource attribute is set to AM Internal.</p>
<dt><code>am.internal_frequency</code></p>
<dd> Specifies the frequency of the internal modulating waveform source. The units are Hertz. </p>
<p> This attribute affects the behavior of the instrument only when the AM ource attribute is set to AM Internal.</p>
<dt><code>am.internal_waveform</code></p>
<dd> Specifies the waveform of the internal modulating waveform source. </p>
<p> This attribute affects the behavior of the instrument only when the AM ource attribute is set to AM Internal. </p>
<p> Values for internal_waveform:</p>
<dt>&bull;</p>
<dd> &#8216;sine&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;square&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;triangle&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;ramp_up&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;ramp_down&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;dc&#8217;</p>
<dt><code>outputs.am.enabled</code></p>
<dd> Specifies whether the function generator applies amplitude modulation to the signal that the function generator produces with the IviFgenStdFunc, IviFgenArbWfm, or IviFgenArbSeq capability groups. If set to True, the function generator applies amplitude modulation to the output signal. If set to False, the function generator does not apply amplitude modulation to the output signal.</p>
<dt><code>outputs.am.source</code></p>
<dd> Specifies the source of the signal that the function generator uses as the modulating waveform. </p>
<p> This attribute affects instrument behavior only when the AM Enabled attribute is set to True.</dl>
<h3><code>ModulateFM</code> class</h3>
<dl>
<dt><code>class ivi.fgen.ModulateFM(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support frequency modulation</p>
<dt><code>fm.configure_internal</code></p>
<dd> Specifies the source of the signal that the function generator uses as the modulating waveform. </p>
<p> This attribute affects instrument behavior only when the FM Enabled attribute is set to True.</p>
<dt><code>fm.internal_deviation</code></p>
<dd> Specifies the maximum frequency deviation, in Hertz, that the function generator applies to the carrier waveform when the FM Source attribute is set to FM Internal. </p>
<p> This attribute affects the behavior of the instrument only when the FM Source attribute is set to FM Internal.</p>
<dt><code>fm.internal_frequency</code></p>
<dd> Specifies the frequency of the internal modulating waveform source. The units are hertz. </p>
<p> This attribute affects the behavior of the instrument only when the FM Source attribute is set to FM Internal.</p>
<dt><code>fm.internal_waveform</code></p>
<dd> Specifies the waveform of the internal modulating waveform source. </p>
<p> This attribute affects the behavior of the instrument only when the FM Source attribute is set to FM Internal. </p>
<p> Values for internal_waveform:</p>
<dt>&bull;</p>
<dd> &#8216;sine&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;square&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;triangle&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;ramp_up&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;ramp_down&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;dc&#8217;</p>
<dt><code>outputs.fm.enabled</code></p>
<dd> Specifies whether the function generator applies amplitude modulation to the carrier waveform. If set to True, the function generator applies frequency modulation to the output signal. If set to False, the function generator does not apply frequency modulation to the output signal.</p>
<dt><code>outputs.fm.source</code></p>
<dd></dl>
<h3><code>SampleClock</code> class</h3>
<dl>
<dt><code>class ivi.fgen.SampleClock(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support external sample clocks</p>
<dt><code>sample_clock.output_enabled</code></p>
<dd> Specifies whether or not the sample clock appears at the sample clock output of the generator.</p>
<dt><code>sample_clock.source</code></p>
<dd> Specifies the clock used for the waveform generation. Note that when using an external sample clock, the Arbitrary Sample Rate attribute must be set to the corresponding frequency of the external sample clock.</dl>
<h3><code>TerminalConfiguration</code> class</h3>
<dl>
<dt><code>class ivi.fgen.TerminalConfiguration(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support single ended or differential output selection</p>
<dt><code>outputs.terminal_configuration</code></p>
<dd> Determines whether the generator will run in single-ended or differential mode, and whether the output gain and offset values will be analyzed based on single-ended or differential operation. </p>
<p> Values for terminal_configuration:</p>
<dt>&bull;</p>
<dd> &#8216;single_ended&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;differential&#8217;</dl>
<h3><code>StartTrigger</code> class</h3>
<dl>
<dt><code>class ivi.fgen.StartTrigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support start triggering</p>
<dt><code>outputs.trigger.start.configure</code></p>
<dd> This function configures the start trigger properties.</p>
<dt><code>outputs.trigger.start.delay</code></p>
<dd> Specifies an additional length of time to delay from the start trigger to the first point in the waveform generation. The units are seconds.</p>
<dt><code>outputs.trigger.start.slope</code></p>
<dd> Specifies the slope of the trigger that starts the generator. </p>
<p> Values for slope:</p>
<dt>&bull;</p>
<dd> &#8216;positive&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;negative&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;either&#8217;</p>
<dt><code>outputs.trigger.start.source</code></p>
<dd> Specifies the source of the start trigger.</p>
<dt><code>outputs.trigger.start.threshold</code></p>
<dd> Specifies the voltage threshold for the start trigger. The units are volts.</p>
<dt><code>trigger.start.configure</code></p>
<dd> This function configures the start trigger properties.</p>
<dt><code>trigger.start.send_software_trigger</code></p>
<dd> This function sends a software-generated start trigger to the instrument.</dl>
<h3><code>StopTrigger</code> class</h3>
<dl>
<dt><code>class ivi.fgen.StopTrigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support stop triggering </p>
<p> <code>ERROR:</code> Unable to execute python code at fgen.rst:1194: </p>
<p> _add_method() takes at most 4 arguments (5 given)</dl>
<h3><code>HoldTrigger</code> class</h3>
<dl>
<dt><code>class ivi.fgen.HoldTrigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support hold triggering</p>
<dt><code>outputs.trigger.hold.configure</code></p>
<dd> This function configures the hold trigger properties.</p>
<dt><code>outputs.trigger.hold.delay</code></p>
<dd> Specifies an additional length of time to delay from the hold trigger to the pause of the generation. The units are seconds.</p>
<dt><code>outputs.trigger.hold.slope</code></p>
<dd> Specifies the slope of the hold trigger. </p>
<p> Values for slope:</p>
<dt>&bull;</p>
<dd> &#8216;positive&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;negative&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;either&#8217;</p>
<dt><code>outputs.trigger.hold.source</code></p>
<dd> Specifies the source of the hold trigger.</p>
<dt><code>outputs.trigger.hold.threshold</code></p>
<dd> Specifies the voltage threshold for the hold trigger. The units are volts.</p>
<dt><code>trigger.hold.configure</code></p>
<dd> This function configures the hold trigger properties.</p>
<dt><code>trigger.hold.send_software_trigger</code></p>
<dd> This function sends a software-generated hold trigger to the instrument.</dl>
<h3><code>ResumeTrigger</code> class</h3>
<dl>
<dt><code>class ivi.fgen.ResumeTrigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support resume triggering</p>
<dt><code>outputs.trigger.resume.configure</code></p>
<dd> This function configures the resume trigger properties.</p>
<dt><code>outputs.trigger.resume.delay</code></p>
<dd> Specifies an additional length of time to delay from the resume trigger to the resumption of the generation. The units are seconds.</p>
<dt><code>outputs.trigger.resume.slope</code></p>
<dd> Specifies the slope of the resume trigger. </p>
<p> Values for slope:</p>
<dt>&bull;</p>
<dd> &#8216;positive&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;negative&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;either&#8217;</p>
<dt><code>outputs.trigger.resume.source</code></p>
<dd> Specifies the source of the resume trigger.</p>
<dt><code>outputs.trigger.resume.threshold</code></p>
<dd> Specifies the voltage threshold for the resume trigger. The units are volts.</p>
<dt><code>trigger.resume.configure</code></p>
<dd> This function configures the resume trigger properties.</p>
<dt><code>trigger.resume.send_software_trigger</code></p>
<dd> This function sends a software-generated resume trigger to the instrument.</dl>
<h3><code>AdvanceTrigger</code> class</h3>
<dl>
<dt><code>class ivi.fgen.AdvanceTrigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for function generators that support advance triggering</p>
<dt><code>outputs.trigger.advance.configure</code></p>
<dd> This function configures the advance trigger properties.</p>
<dt><code>outputs.trigger.advance.delay</code></p>
<dd> Specifies an additional length of time to delay from the advance trigger to the advancing to the end of the current waveform. Units are seconds.</p>
<dt><code>outputs.trigger.advance.slope</code></p>
<dd> Specifies the slope of the advance trigger. </p>
<p> Values for slope:</p>
<dt>&bull;</p>
<dd> &#8216;positive&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;negative&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;either&#8217;</p>
<dt><code>outputs.trigger.advance.source</code></p>
<dd> Specifies the source of the advance trigger.</p>
<dt><code>outputs.trigger.advance.threshold</code></p>
<dd> Specifies the voltage threshold for the advance trigger. The units are volts.</p>
<dt><code>trigger.advance.configure</code></p>
<dd> This function configures the advance trigger properties.</p>
<dt><code>trigger.advance.send_software_trigger</code></p>
<dd> This function sends a software-generated advance trigger to the instrument.</dl>
<h2>IVI.DCPWR &#8212; DC POWER SUPPLY CLASS</h2>
<p> This module provides the base functionality for DC power supplies.</p>
<h3>Functions and Exceptions</h3>
<dl>
<dt><code>exception ivi.dcpwr.IviException</code></p>
<dd> Exception raised on various occasions; argument is a string describing what is wrong.</dl>
<h3><code>Base</code> class</h3>
<dl>
<dt><code>class ivi.dcpwr.Base(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Base IVI methods for all DC power supplies</p>
<dt><code>outputs[].configure_current_limit</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.3.1</i> </p>
<p> This function configures the current limit. It specifies the output current limit value and the behavior of the power supply when the output current is greater than or equal to that value. </p>
<p> See the definition of the Current Limit Behavior attribute for defined values for the behavior parameter.</p>
<dt><code>outputs[].configure_ovp</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.3.4</i> </p>
<p> Configures the over-voltage protection. It specifies the over-voltage limit and the behavior of the power supply when the output voltage is greater than or equal to that value. </p>
<p> When the Enabled parameter is False, the Limit parameter does not affect the instrument&#8217;s behavior, and the driver does not set the OVP Limit attribute.</p>
<dt><code>outputs[].configure_range</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.3.3</i> </p>
<p> Configures the power supply&#8217;s output range on an output. One parameter specifies whether to configure the voltage or current range, and the other parameter is the value to which to set the range. </p>
<p> Setting a voltage range can invalidate a previously configured current range. Setting a current range can invalidate a previously configured voltage range.</p>
<dt><code>outputs[].current_limit</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.2.1</i> </p>
<p> Specifies the output current limit. The units are Amps. </p>
<p> The value of the Current Limit Behavior attribute determines the behavior of the power supply when the output current is equal to or greater than the value of this attribute.</p>
<dt><code>outputs[].current_limit_behavior</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.2.2</i> </p>
<p> Specifies the behavior of the power supply when the output current is equal to or greater than the value of the Current Limit attribute. </p>
<p> Values</p>
<dt>&bull;</p>
<dd> &#8216;trip&#8217; &#8211; The power supply disables the output when the output current is equal to or greater than the value of the Current Limit attribute.</p>
<dt>&bull;</p>
<dd> &#8216;regulate&#8217; &#8211; The power supply restricts the output voltage such that the output current is not greater than the value of the Current Limit attribute.</p>
<dt><code>outputs[].enabled</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.2.3</i> </p>
<p> If true, the signal the power supply produces appears at the output connector. If false, the signal the power supply produces does not appear at the output connector.</p>
<dt><code>outputs[].name</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.2.9</i> </p>
<p> This attribute returns the repeated capability identifier defined by specific driver for the output channel that corresponds to the index that the user specifies. If the driver defines a qualified Output Channel name, this property returns the qualified name. </p>
<p> If the value that the user passes for the Index parameter is less than zero or greater than the value of the Output Channel Count, the attribute raises a SelectorRangeException.</p>
<dt><code>outputs[].ovp_enabled</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.2.4</i> </p>
<p> Specifies whether the power supply provides over-voltage protection. If this attribute is set to True, the power supply disables the output when the output voltage is greater than or equal to the value of the OVP Limit attribute.</p>
<dt><code>outputs[].ovp_limit</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.2.5</i> </p>
<p> Specifies the voltage the power supply allows. The units are Volts. </p>
<p> If the OVP Enabled attribute is set to True, the power supply disables the output when the output voltage is greater than or equal to the value of this attribute. </p>
<p> If the OVP Enabled is set to False, this attribute does not affect the behavior of the instrument.</p>
<dt><code>outputs[].query_current_limit_max</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.3.7</i> </p>
<p> This function returns the maximum programmable current limit that the power supply accepts for a particular voltage level on an output.</p>
<dt><code>outputs[].query_output_state</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.3.9</i> </p>
<p> This function returns whether the power supply is in a particular output state. </p>
<p> A constant voltage condition occurs when the output voltage is equal to the value of the Voltage Level attribute and the current is less than or equal to the value of the Current Limit attribute. </p>
<p> A constant current condition occurs when the output current is equal to the value of the Current Limit attribute and the Current Limit Behavior attribute is set to the Current Regulate defined value. </p>
<p> An unregulated condition occurs when the output voltage is less than the value of the Voltage Level attribute and the current is less than the value of the Current Limit attribute. </p>
<p> An over-voltage condition occurs when the output voltage is equal to or greater than the value of the OVP Limit attribute and the OVP Enabled attribute is set to True. </p>
<p> An over-current condition occurs when the output current is equal to or greater than the value of the Current Limit attribute and the Current Limit Behavior attribute is set to the Current Trip defined value. </p>
<p> When either an over-voltage condition or an over-current condition occurs, the power supply&#8217;s output protection disables the output. If the power supply is in an over-voltage or over-current state, it does not produce power until the output protection is reset. The Reset Output Protection function resets the output protection. Once the output protection is reset, the power supply resumes generating a power signal. </p>
<p> Values for output_state:</p>
<dt>&bull;</p>
<dd> &#8216;constant_voltage&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;constant_current&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;over_voltage&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;over_current&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;unregulated&#8217;</p>
<dt><code>outputs[].query_voltage_level_max</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.3.8</i> </p>
<p> This function returns the maximum programmable voltage level that the power supply accepts for a particular current limit on an output.</p>
<dt><code>outputs[].reset_output_protection</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.3.10</i> </p>
<p> This function resets the power supply output protection after an over-voltage or over-current condition occurs. </p>
<p> An over-voltage condition occurs when the output voltage is equal to or greater than the value of the OVP Limit attribute and the OVP Enabled attribute is set to True. </p>
<p> An over-current condition occurs when the output current is equal to or greater than the value of the Current Limit attribute and the Current Limit Behavior attribute is set to Current Trip. </p>
<p> When either an over-voltage condition or an over-current condition occurs, the output protection of the power supply disables the output. Once the output protection is reset, the power supply resumes generating a power signal. </p>
<p> Use the Query Output State function to determine if the power supply is in an over-voltage or over-current state.</p>
<dt><code>outputs[].voltage_level</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrBase, section 4.2.6</i> </p>
<p> Specifies the voltage level the DC power supply attempts to generate. The units are Volts.</dl>
<h3><code>Trigger</code> class</h3>
<dl>
<dt><code>class ivi.dcpwr.Trigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for power supplies supporting trigger based output changes</p>
<dt><code>outputs[].trigger_source</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrTrigger, section 5.2.1</i> </p>
<p> Specifies the trigger source. After an Initiate call, the power supply waits for a trigger event from the source specified with this attribute. After a trigger event occurs, the power supply changes the voltage level to the value of the Triggered Voltage Level attribute and the current limit to the value of the Triggered Current Limit attribute.</p>
<dt><code>outputs[].triggered_current_limit</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrTrigger, section 5.2.2</i> </p>
<p> Specifies the value to which the power supply sets the current limit after a trigger event occurs. The units are Amps. </p>
<p> After an Initiate call, the power supply waits for a trigger event from the source specified with the Trigger Source attribute. After a trigger event occurs, the power supply sets the current limit to the value of this attribute. </p>
<p> After a trigger occurs, the value of the Current Limit attribute reflects the new value to which the current limit has been set.</p>
<dt><code>outputs[].triggered_voltage_level</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrTrigger, section 5.2.3</i> </p>
<p> Specifies the value to which the power supply sets the voltage level after a trigger event occurs. The units are Volts. </p>
<p> After an Initiate call, the power supply waits for a trigger event from the source specified with the Trigger Source attribute. After a trigger event occurs, the power supply sets the voltage level to the value of this attribute. </p>
<p> After a trigger occurs, the value of the Voltage Level attribute reflects the new value to which the voltage level has been set.</p>
<dt><code>trigger.abort</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrTrigger, section 5.3.1</i> </p>
<p> If the power supply is currently waiting for a trigger to change the output signal, this function returns the power supply to the ignore triggers state. </p>
<p> If the power supply is not waiting for a trigger, this function does nothing and returns Success.</p>
<dt><code>trigger.initiate</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrTrigger, section 5.3.5</i> </p>
<p> If the power supply is not currently waiting for a trigger, this function causes the power supply to wait for a trigger. </p>
<p> If the power supply is already waiting for a trigger, this function does nothing and returns Success.</dl>
<h3><code>SoftwareTrigger</code> class</h3>
<dl>
<dt><code>class ivi.dcpwr.SoftwareTrigger(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for power supplies supporting software triggering</p>
<dt><code>ivi.dcpwr.send_software_trigger</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrSoftwareTrigger, section 6.2.1</i> </p>
<p> This function sends a software-generated trigger to the instrument. It is only applicable for instruments using interfaces or protocols which support an explicit trigger function. For example, with GPIB this function could send a group execute trigger to the instrument. Other implementations might send a <code>*TRG</code> command. </p>
<p> Since instruments interpret a software-generated trigger in a wide variety of ways, the precise response of the instrument to this trigger is not defined. Note that SCPI details a possible implementation. </p>
<p> This function should not use resources which are potentially shared by other devices (for example, the VXI trigger lines). Use of such shared resources may have undesirable effects on other devices. </p>
<p> This function should not check the instrument status. Typically, the end-user calls this function only in a sequence of calls to other low-level driver functions. The sequence performs one operation. The end-user uses the low-level functions to optimize one or more aspects of interaction with the instrument. To check the instrument status, call the appropriate error query function at the conclusion of the sequence. </p>
<p> The trigger source attribute must accept Software Trigger as a valid setting for this function to work. If the trigger source is not set to Software Trigger, this function does nothing and returns the error Trigger Not Software.</dl>
<h3><code>Measurement</code> class</h3>
<dl>
<dt><code>class ivi.dcpwr.Measurement(*args, **kwargs)</code></p>
<dd> Bases: <code>ivi.ivi.IviContainer</code> </p>
<p> Extension IVI methods for power supplies supporting measurement of the output signal</p>
<dt><code>outputs[].measure</code></p>
<dd> <i>IVI class IviDCPwr, capability group IviDCPwrMeasurement, section 7.2.1</i> </p>
<p> Takes a measurement on the output signal and returns the measured value. </p>
<p> Values for measurement_type:</p>
<dt>&bull;</p>
<dd> &#8216;voltage&#8217;</p>
<dt>&bull;</p>
<dd> &#8216;current&#8217;</dl>
<h2>WRITING NEW PYTHON IVI DRIVERS</h2>
<p> First, you&#8217;re going to need to download the IVI specification for the type of instrument you have from the IVI foundation. This isn&#8217;t completely necessary, but there is a lot of information in the spec about the specific functionality of various commands that isn&#8217;t in the source code. I suppose this should probably be changed, but the spec is freely available so it isn&#8217;t that big of an issue. You only need to download the spec for your type of device (IviFgen, IviScope, etc.). You&#8217;re also going to need to download the programming guide for your instrument, if you haven&#8217;t already. </p>
<p> Now that you know what instrument class your instrument is, you should create a file for it in the proper subdirectory with the proper name. Note that supporting several instruments in the same line is pretty easy, just look at some of the other files for reference. I would highly recommend creating wrappers for all of the instruments in the series even if you don&#8217;t have any on hand for testing. You also will need to add a line (or several lines) to <code>__init__.py</code> in the same directory so that the instrument files are loaded automatically with python-ivi and don&#8217;t need to be loaded individually. </p>
<p> The structure of the individual driver files is quite simple. Take a look at the existing files for reference. Start by adding the header comment and license information. Then add the correct includes. At minimum, you will need to include ivi and the particular instrument class that you need from the parent directory (<code>from .. include ivi</code>). After that, you can specify any constants and/or mappings that the instrument requires. IVI specifies one set of standard configuration values for a lot of functions and this does not necessarily agree with the instrument&#8217;s firmware, so it&#8217;s likely you will need to redefine several of these lists as mappings to make writing the code easier. This can be done incrementally while the driver functionality is being implemented. </p>
<p> Next, you need to add the class definition. The name should match the file name, and it will derive from ivi.Driver and the supported subclasses of your instrument. Go over the IVI spec and the programming guide and see what subclasses are supported by seeing which functions are supported by the instrument. There isn&#8217;t always going to be a 1:1 mapping &#8211; there will likely be functions that the instrument does not support but IVI has a wrapper for, and there will likely be functions that IVI does not have a wrapper for but the instrument does support that may be very useful. You should add a subclass if any portion of its functionality is supported by the instrument. </p>
<p> After that, you need to define the functions common to all IVI drivers. You can just copy everything from init to utility_unlock_object from an existing driver and then update everything for your instrument. Generally all this code will be very similar. Take a look at some of the existing drivers for reference. Very important: any <code>super()</code> calls must be updated so that the class name matches (requirement for Python 2). You should also remove all of the initialization in <code>__init__</code> that you don&#8217;t need &#8211; the bare minimum is <code>_instrument_id</code> and all of the <code>_identity</code> values. For some instruments, you&#8217;re going to need to specify channel counts as well as an <code>_init_channels</code> or <code>_init_outputs</code> method. Note that if one of these methods is needed, it cannot be empty as it must at least have a call to super so that all of the proper init methods are called. At this point, you can test the connection to the equipment to make sure it is communicating and reading out the ID properly. </p>
<p> Testing you code is actually pretty straightforward; you don&#8217;t need to re-install the library to test it; just make sure to instantiate it while you&#8217;re running in the same directory as the ivi folder (not inside). I recommend ipython for testing. Unfortulatey, the auto reload doesn&#8217;t work very well for python-ivi, so you&#8217;ll need to restart ipython every time you change something. However, it supports history and autocompletion, so after you import IVI once, you can just type &#8216;imp&#8217; and hit the up arrow until &#8216;import ivi&#8217; shows up. </p>
<p> Test the interface and identity query by instantiating your driver and connecting to the instrument by running something like this in ipython: </p>
<pre>
&gt;&gt;&gt; import ivi
&gt;&gt;&gt; mso = ivi.agilent.agilentMSO7104A(&quot;TCPIP0::192.168.1.104::INSTR&quot;)
&gt;&gt;&gt; mso.identity.instrument_model
</pre>
<p> If everything is working, the instrument&#8217;s model number will be displayed. Once you get this working, you can move on to implementing the actual functionality. </p>
<p> Start by copying in all of the bare function definitions from the driver file. Copy all of the get and _set function definitions from the ivi driver file for the Base class and all of the subclasses that you are implementing. You also need any methods whose only implementation is &#8216;pass&#8217;. The ones that call other methods can generally be left out as the default implementation should be fine. You may also want to copy some of the instance variable initializations from the <code>__init__</code> method as well if you need different defaults. These should be added to the init method you created earlier for your instrument. </p>
<p> Finally, you need to go write python code for all of the functions that the instrument supports. Take a look at some <code>_get</code>/<code>_set</code> pairs for some of the existing drivers to see the format. It&#8217;s rather straightforward but quite tedious.</p>
<h3>Driver Template</h3>
<p> This is a sample template driver that incorporates all of the major components. It is drawn from the Agilent 7000 series driver. Template: </p>
<pre><code>
"""
Python Interchangeable Virtual Instrument Library
Copyright (c) 2012 Alex Forencich
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import struct
from .. import ivi
from .. import scope
AcquisitionTypeMapping = {
        'normal': 'norm',
        'peak_detect': 'peak',
        'high_resolution': 'hres',
        'average': 'aver'}
#more instrument - specific sets and mappings
class agilent7000(ivi.Driver, scope.Base, scope.TVTrigger,
                scope.GlitchTrigger, scope.WidthTrigger, scope.AcLineTrigger,
                scope.WaveformMeasurement, scope.MinMaxWaveform,
                scope.ContinuousAcquisition, scope.AverageAcquisition,
                scope.SampleMode, scope.AutoSetup):
    "Agilent InfiniiVision 7000 series IVI oscilloscope driver"
    def __init__(self, *args, **kwargs):
        self._analog_channel_name = list()
        self._analog_channel_count = 4
        self._digital_channel_name = list()
        self._digital_channel_count = 16
        self._channel_label = list()
#other per - channel instrument - specific variables that are
#referenced in _init_channels
        super(agilent7000, self).__init__(*args, **kwargs)
        self._instrument_id = 'AGILENT TECHNOLOGIES'
        self._analog_channel_name = list()
        self._analog_channel_count = 4
        self._digital_channel_name = list()
        self._digital_channel_count = 16
        self._channel_count = 20
        self._bandwidth = 1e9
#initialize other instrument - specific variables
        self._identity_description = "Agilent InfiniiVision 7000 series IVI oscilloscope driver"
        self._identity_identifier = ""
        self._identity_revision = ""
        self._identity_vendor = ""
        self._identity_instrument_manufacturer = "Agilent Technologies"
        self._identity_instrument_model = ""
        self._identity_instrument_firmware_revision = ""
        self._identity_specification_major_version = 4
        self._identity_specification_minor_version = 1
        self._identity_supported_instrument_models =['DSO7012A','DSO7014A','DSO7032A',
                'DSO7034A','DSO7052A','DSO7054A','DSO7104A','MSO7012A','MSO7014A','MSO7032A',
                'MSO7034A','MSO7052A','MSO7054A','MSO7104A','DSO7012B','DSO7014B','DSO7032B',
                'DSO7034B','DSO7052B','DSO7054B','DSO7104B','MSO7012B','MSO7014B','MSO7032B',
                'MSO7034B','MSO7052B','MSO7054B','MSO7104B']
        self.channels._add_property('label',
                        self._get_channel_label,
                        self._set_channel_label,
                        None,
                        """
                        Custom property documentation
                        """)
#other instrument specific properties
        self._init_channels()
    def initialize(self, resource = None, id_query = False, reset = False, **keywargs):
        "Opens an I/O session to the instrument."
        self._channel_count = self._analog_channel_count + self._digital_channel_count
        super(agilent7000, self).initialize(resource, id_query, reset, **keywargs)
#interface clear
        if not self._driver_operation_simulate:
            self._clear()
#check ID
        if id_query and not self._driver_operation_simulate:
            id = self.identity.instrument_model
            id_check = self._instrument_id
            id_short = id[:len(id_check)]
            if id_short != id_check:
                raise Exception("Instrument ID mismatch, expecting %s, got %s", id_check, id_short)
#reset
        if reset:
            self.utility.reset()
    def _load_id_string(self):
        if self._driver_operation_simulate:
            self._identity_instrument_manufacturer = "Not available while simulating"
            self._identity_instrument_model = "Not available while simulating"
            self._identity_instrument_firmware_revision = "Not available while simulating"
        else:
            lst = self._ask("*IDN?").split(",")
            self._identity_instrument_manufacturer = lst[0]
            self._identity_instrument_model = lst[1]
            self._identity_instrument_firmware_revision = lst[3]
            self._set_cache_valid(True, 'identity_instrument_manufacturer')
            self._set_cache_valid(True, 'identity_instrument_model')
            self._set_cache_valid(True, 'identity_instrument_firmware_revision')
    def _get_identity_instrument_manufacturer(self):
        if self._get_cache_valid():
            return self._identity_instrument_manufacturer
        self._load_id_string()
        return self._identity_instrument_manufacturer
    def _get_identity_instrument_model(self):
        if self._get_cache_valid():
            return self._identity_instrument_model
        self._load_id_string()
        return self._identity_instrument_model
    def _get_identity_instrument_firmware_revision(self):
        if self._get_cache_valid():
            return self._identity_instrument_firmware_revision
        self._load_id_string()
        return self._identity_instrument_firmware_revision
    def _utility_disable(self):
        pass
    def _utility_error_query(self):
        error_code = 0
        error_message = "No error"
        if not self._driver_operation_simulate:
            error_code, error_message = self._ask(":system:error?").split(',')
            error_code = int(error_code)
            error_message = error_message.strip(' "')
        return (error_code, error_message)
    def _utility_lock_object(self):
        pass
    def _utility_reset(self):
        if not self._driver_operation_simulate:
            self._write("*RST")
            self.driver_operation.invalidate_all_attributes()
    def _utility_reset_with_defaults(self):
        self._utility_reset()
    def _utility_self_test(self):
        code = 0
        message = "Self test passed"
        if not self._driver_operation_simulate:
            code = int(self._ask("*TST?"))
            if code != 0:
                message = "Self test failed"
        return (code, message)
    def _utility_unlock_object(self):
        pass
    def _init_channels(self):
        super(agilent7000, self)._init_channels()
        self._channel_name = list()
        self._channel_label = list()
#init per - channel instrument - specific variables
        for i in range(self._channel_count):
            self._channel_name.append("channel%d" % (i+1))
            self._channel_label.append("%d" % (i+1))
#init per - channel instrument - specific variables
        self.channels._set_list(self._channel_name)
    def _get_acquisition_start_time(self):
        pos = 0
        if not self._driver_operation_simulate and not self._get_cache_valid():
            pos = float(self._ask(":timebase:position?"))
            self._set_cache_valid()
        self._acquisition_start_time = pos - self._get_acquisition_time_per_record() * 5 / 10
        return self._acquisition_start_time
    def _set_acquisition_start_time(self, value):
        value = float(value)
        value = value + self._get_acquisition_time_per_record() * 5 / 10
        if not self._driver_operation_simulate:
            self._write(":timebase:position %e" % value)
        self._acquisition_start_time = value
        self._set_cache_valid()
#more definitions
</code></pre>
<h2>APPENDIX</h2>
<h3>License</h3>
<p> Copyright (c) 2012-2014 Alex Forencich </p>
<p> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: </p>
<p> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. </p>
<p> THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</p>
<dl>
<dt>&bull;</p>
<dd> <i>genindex</i></p>
<dt>&bull;</p>
<dd> <i>modindex</i></p>
<dt>&bull;</p>
<dd> <i>search</i></dl>
<h2>AUTHOR</h2>
<p> Alex Forencich</p>
<h2>COPYRIGHT</h2>
<p> 2012-2014, Alex Forencich </p>
<h2>Index</h2>
<dt><a href="#lbBA">IVI.SCOPE &#8212; OSCILLOSCOPE CLASS</a></p>
<dd>
<dt><a href="#lbBR">IVI.FGEN &#8212; FUNCTION GENERATOR CLASS</a></p>
<dd>
<dt><a href="#lbCR">IVI.DCPWR &#8212; DC POWER SUPPLY CLASS</a></p>
<dd>
<dt><a href="#lbCX">WRITING NEW PYTHON IVI DRIVERS</a></p>
<dd>
<dt><a href="#lbCZ">APPENDIX</a></p>
<dd>
<dt><a href="#lbDB">AUTHOR</a></p>
<dd>
<dt><a href="#lbDC">COPYRIGHT</a></p>
<dd></dl>
