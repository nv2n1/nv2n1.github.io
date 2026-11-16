---
title: "libipmimonitoring(5)"
name: "libipmimonitoring"
section: "5"
letter: "l"
url: "/docs/linux/man/5-libipmimonitoring/"
description: "ipmi_monitoring_sensors.conf – specify sensor interpretation rules"
---

<p>ipmi_monitoring_sensors.conf &#8211; specify sensor interpretation rules</p>
<h2>Description</h2>
<p>The <code>/etc/ipmi_monitoring_sensors.conf</code> defines how IPMI sensors should be interpreted. IPMI based sensors specify a number of states/thresholds when they are read. Based on those states/thresholds we can allow the <code><a href="/docs/linux/man/3-libipmimonitoring/">libipmimonitoring</a>(3)</code> library and <code><a href="/docs/linux/man/8-ipmimonitoring/">ipmimonitoring</a>(8)</code> tool to report if a sensor reading is &quot;good&quot; or &quot;bad&quot; (or in a NOMINAL, WARNING, or CRITICAL state). Each of the states listed below are (hopefully) descriptive enough to describe the state conditions that may be set/unset for each sensor type. For more detailed information on each of the individual states listed below, please see the IPMI Specification &quot;Sensor and Event Code Tables&quot;. <code><a href="/docs/linux/man/8-ipmi-sensors/">Ipmi-sensors</a>(8)</code> can be used to determine the sensor types and the states/thresholds that exist on a system by outputting very verbose output and seeing what types of Assertion or Deassertion events are possible. The possible values for all states/thresholds below are: Nominal &#8211; Signal Nominal reading if state/threshold tripped Warning &#8211; Signal Warning reading if state/treshold tripped Critical &#8211; Signal Critical reading if state/threshold tripped Not all IPMI sensor types and event types are currently supported. If you would like more to be supported, please e-mail the FreeIPMI mailing list. The default values selected for individual states/thresholds being tripped are based on best guesses and motherboards being analyzed. If you think they should be changed, please e-mail the FreeIPMI mailing list to discuss what the defaults should be. Most default interpretations can be determined quite easily and can meet the needs of most users. For example, a reading of &quot;Performance_Met&quot; is normally better than &quot;Performance_Lags&quot;. However, some sensors can be ambiguous and depend completely on the manufacturer. For example, &quot;State_Asserted&quot; vs. &quot;State_Deasserted&quot; are completely at the interpretation of the vendor. Users are advised to adjust the interpretations below as needed for their machines. </p>
<h2>Format</h2>
<p>The configuration options that can be specified in the configuration file are listed below. Each configuration option must be listed on a separate line. Arguments for an option are separated by any amount of whitespace. Multiple arguments are also separated by whitespace. Comments can be marked by using the pound sign (&quot;#&quot;) character, and lines can be continued on the next using backslash (&quot;\&quot;). </p>
<p> Note that it is possible to list the username, password and other potentially sensitive information in the configuration file. If this data is stored in a configuration file, system administrators should limit access to this file.</p>
<h2>Options</h2>
<dl>
<dt><code>IPMI_Threshold_Sensor</code></dt>
<dd>The following states correspond to threshold sensors. This normally applies to sensors that measure non-discrete values, such as temperatures, voltages, RPM, etc.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Threshold_Sensor_At_Or_Below_Lower_Non_Critical_Threshold</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Threshold_Sensor_At_Or_Below_Lower_Critical_Threshold</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Threshold_Sensor_At_Or_Below_Lower_Non_Recoverable_Threshold</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Threshold_Sensor_At_Or_Above_Upper_Non_Critical_Threshold</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Threshold_Sensor_At_Or_Above_Upper_Critical_Threshold</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Threshold_Sensor_At_Or_Above_Upper_Non_Recoverable_Threshold</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Voltage_State</code></dt>
<dd>The following states correspond to Voltage sensors that report an assertion or deassertion.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Voltage_State_Deasserted</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Voltage_State_Asserted</code></dt>
<dd>Defaults to Warning.</dd></dl>
</dl>
<dt><code>IPMI_Voltage_Performance</code></dt>
<dd>The following states correspond to Voltage sensors that report on performance.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Voltage_Performance_Met</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Voltage_Performance_Lags</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Fan_Device_Install</code></dt>
<dd>The following states correspond to Fan sensors that report on device installation.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Fan_Device_Install_Device_Removed_Device_Absent</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Fan_Device_Install_Device_Inserted_Device_Present</code></dt>
<dd>Defaults to Nominal.</dd></dl>
</dl>
<dt><code>IPMI_Fan_Transition_Availability</code></dt>
<dd>The following states correspond to Fan sensors that report on device availability.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Fan_Transition_Availability_To_Running</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Fan_Transition_Availability_To_In_Test</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Fan_Transition_Availability_To_Power_Off</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Fan_Transition_Availability_To_On_Line</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Fan_Transition_Availability_To_Off_Line</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Fan_Transition_Availability_To_Off_Duty</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Fan_Transition_Availability_To_Degraded</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Fan_Transition_Availability_To_Power_Save</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Fan_Transition_Availability_Install_Error</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Fan_Redundancy</code></dt>
<dd>The following states correspond to Fan sensors that report on redundancy.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Fan_Redundancy_Fully_Redundant</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Fan_Redundancy_Redundancy_Lost</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Fan_Redundancy_Redundancy_Degraded</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Fan_Redundancy_Non_Redundant_Sufficient_Resources_From_Redundant</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Fan_Redundancy_Non_Redundant_Sufficient_Resources_From_Insufficient_Redundancy</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Fan_Redundancy_Non_Redundant_Insufficient_Resources</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Fan_Redundancy_Redundancy_Degraded_From_Fully_Redundant</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Fan_Redundancy_Redundancy_Degraded_From_Non_Redundant</code></dt>
<dd>Defaults to Warning.</dd></dl>
</dl>
<dt><code>IPMI_Processor_State</code></dt>
<dd>The following states correspond to Processor sensors that report an assertion or deassertion.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Processor_State_Deasserted</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Processor_State_Asserted</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Power_Supply_State</code></dt>
<dd>The following states correspond to Power_Supply sensors that report an assertion or deassertion.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Power_Supply_State_Deasserted</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Supply_State_Asserted</code></dt>
<dd>Defaults to Nominal.</dd></dl>
</dl>
<dt><code>IPMI_Power_Supply_Redundancy</code></dt>
<dd>The following states correspond to Power Supply sensors that report on redundancy.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Power_Supply_Redundancy_Fully_Redundant</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Power_Supply_Redundancy_Redundancy_Lost</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Supply_Redundancy_Redundancy_Degraded</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Power_Supply_Redundancy_Non_Redundant_Sufficient_Resources_From_Redundant</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Supply_Redundancy_Non_Redundant_Sufficient_Resources_From_Insufficient_Redundancy</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Supply_Redundancy_Non_Redundant_Insufficient_Resources</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Supply_Redundancy_Redundancy_Degraded_From_Fully_Redundant</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Power_Supply_Redundancy_Redundancy_Degraded_From_Non_Redundant</code></dt>
<dd>Defaults to Warning.</dd></dl>
</dl>
<dt><code>IPMI_Power_Unit_Device_Install</code></dt>
<dd>The following states correspond to Power Unit sensors that report on device installation.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Power_Unit_Device_Install_Device_Removed_Device_Absent</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Unit_Device_Install_Device_Inserted_Device_Present</code></dt>
<dd>Defaults to Nominal.</dd></dl>
</dl>
<dt><code>IPMI_Power_Unit_Redundancy</code></dt>
<dd>The following states correspond to Power Unit sensors that report on redundancy.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Power_Unit_Redundancy_Fully_Redundant</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Power_Unit_Redundancy_Redundancy_Lost</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Unit_Redundancy_Redundancy_Degraded</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Power_Unit_Redundancy_Non_Redundant_Sufficient_Resources_From_Redundant</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Unit_Redundancy_Non_Redundant_Sufficient_Resources_From_Insufficient_Redundancy</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Unit_Redundancy_Non_Redundant_Insufficient_Resources</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Unit_Redundancy_Redundancy_Degraded_From_Fully_Redundant</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Power_Unit_Redundancy_Redundancy_Degraded_From_Non_Redundant</code></dt>
<dd>Defaults to Warning.</dd></dl>
</dl>
<dt><code>IPMI_Module_Board_State</code></dt>
<dd>The following states correspond to Module/Board sensors that report an assertion or deassertion.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Module_Board_State_Deasserted</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Module_Board_State_Asserted</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Module_Board_Device_Install</code></dt>
<dd>The following states correspond to Module/Board sensors that report on device installation.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Module_Board_Device_Install_Device_Removed_Device_Absent</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Module_Board_Device_Install_Device_Inserted_Device_Present</code></dt>
<dd>Defaults to Nominal.</dd></dl>
</dl>
<dt><code>IPMI_Drive_Slot_State</code></dt>
<dd>The following states correspond to Drive Slot sensors that report an assertion or deassertion.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Drive_Slot_State_Deasserted</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Drive_Slot_State_Asserted</code></dt>
<dd>Defaults to Nominal.</dd></dl>
</dl>
<dt><code>IPMI_Drive_Slot_Predictive_Failure</code></dt>
<dd>The following states correspond to Drive_Slot sensors that report a predictive failure assertion or deassertion.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Drive_Slot_Predictive_Failure_Deasserted</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Drive_Slot_Predictive_Failure_Asserted</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Drive_Slot_Device_Install</code></dt>
<dd>The following states correspond to Drive Slot sensors that report on device installation.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Drive_Slot_Device_Install_Device_Removed_Device_Absent</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Drive_Slot_Device_Install_Device_Inserted_Device_Present</code></dt>
<dd>Defaults to Nominal.</dd></dl>
</dl>
<dt><code>IPMI_Button_Switch_State</code></dt>
<dd>The following states correspond to Button/Switch sensors that report an assertion or deassertion.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Button_Switch_State_Deasserted</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Button_Switch_State_Asserted</code></dt>
<dd>Defaults to Nominal.</dd></dl>
</dl>
<dt><code>IPMI_Entity_Presence_Device_Install</code></dt>
<dd>The following states correspond to Entity Presence sensors that report on device installation.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Entity_Presence_Device_Install_Device_Removed_Device_Absent</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Entity_Presence_Device_Install_Device_Inserted_Device_Present</code></dt>
<dd>Defaults to Nominal.</dd></dl>
</dl>
<dt><code>IPMI_Physical_Security</code></dt>
<dd>The following states correspond to Physical Security sensors w/ Physical Security specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Physical_Security_General_Chassis_Intrusion</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Physical_Security_Drive_Bay_Intrusion</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Physical_Security_IO_Card_Intrusion</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Physical_Security_Processor_Area_Intrusion</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Physical_Security_LAN_Leash_Lost</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Physical_Security_Unauthorized_Dock_Undock</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Physical_Security_FAN_Area_Intrusion</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Platform_Security_Violation_Attempt</code></dt>
<dd>The following states correspond to Platform Violation Attempt sensors w/ Platform Security Violation Attempt specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Platform_Security_Violation_Attempt_Secure_Mode_Violation_Attempt</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Platform_Security_Violation_Attempt_Pre_Boot_Password_Violation_User_Password</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Platform_Security_Violation_Attempt_Pre_Boot_Password_Violation_Setup_Password</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Platform_Security_Violation_Attempt_Pre_Boot_Password_Violation_Network_Boot_Password</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Platform_Security_Violation_Attempt_Other_Pre_Boot_Password_Violation</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Platform_Security_Violation_Attempt_Out_Of_Band_Access_Password_Violation</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Processor</code></dt>
<dd>The following states correspond to Processor sensors w/ Processor specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Processor_IERR</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Processor_Thermal_Trip</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Processor_FRB1_BIST_Failure</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Processor_FRB2_Hang_In_POST_Failure</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Processor_FRB3_Processor_Startup_Initialization_Failure</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Processor_Configuration_Error</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Processor_SMBIOS_Uncorrectable_CPU_Complex_Error</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Processor_Processor_Presence_Detected</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Processor_Processor_Disabled</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Processor_Terminator_Presence_Detected</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Processor_Processor_Automatically_Throttled</code></dt>
<dd>Defaults to Warning.</dd></dl>
</dl>
<dt><code>IPMI_Power_Supply</code></dt>
<dd>The following states correspond to Power Supply sensors w/ Power Supply specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Power_Supply_Presence_Detected</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Power_Supply_Power_Supply_Failure_Detected</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Supply_Predictive_Failure</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Supply_Power_Supply_Input_Lost_AC_DC</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Supply_Power_Supply_Input_Lost_Or_Out_Of_Range</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Supply_Power_Supply_Input_Out_Of_Range_But_Present</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Supply_Configuration_Error</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Power_Unit</code></dt>
<dd>The following states correspond to Power Unit sensors w/ Power Unit specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Power_Unit_Power_Off_Power_Down</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Power_Unit_Power_Cycle</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Power_Unit_240VA_Power_Down</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Power_Unit_Interlock_Power_Down</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Power_Unit_AC_Lost</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Unit_Soft_Power_Control_Failure</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Unit_Power_Unit_Failure_Detected</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Power_Unit_Predictive_Failure</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Memory</code></dt>
<dd>The following states correspond to Memory sensors w/ Memory specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Memory_Correctable_ECC_Memory_Error</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Memory_Uncorrectable_ECC_Memory_Error</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Memory_Parity</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Memory_Memory_Scrub_Failed</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Memory_Memory_Device_Disabled</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Memory_Correctable_ECC_Memory_Error_Logging_Limit_Reached</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Memory_Presence_Detected</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Memory_Configuration_Error</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Memory_Spare</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Memory_Memory_Automatically_Throttled</code></dt>
<dd>Defaults to Warning.</dd></dl>
</dl>
<dt><code>IPMI_Drive_Slot</code></dt>
<dd>The following states correspond to Drive Slot sensors w/ Drive Slot specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Drive_Slot_Drive_Presence</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Drive_Slot_Drive_Fault</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Drive_Slot_Predictive_Failure</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Drive_Slot_Hot_Spare</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Drive_Slot_Consistency_Check_Parity_Check_In_Progress</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Drive_Slot_In_Critical_Array</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Drive_Slot_In_Failed_Array</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Drive_Slot_Rebuild_Remap_In_Progress</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Drive_Slot_Rebuild_Remap_Aborted</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_System_Firmware_Progress</code></dt>
<dd>The following states correspond to System Firmware Progress sensors w/ System Firmware Progress specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_System_Firmware_Progress_System_Firmware_Error</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_System_Firmware_Progress_System_Firmware_Hang</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_System_Firmware_Progress_System_Firmware_Progress</code></dt>
<dd>Defaults to Nominal.</dd></dl>
</dl>
<dt><code>IPMI_Event_Logging_Disabled</code></dt>
<dd>The following states correspond to Event Logging Disabled sensors w/</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Event_Logging_Disabled_Correctable_Memory_Logging_Disabled</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Event_Logging_Disabled_Event_Type_Logging_Disabled</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Event_Logging_Disabled_Log_Area_Reset_Cleared</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Event_Logging_Disabled_All_Event_Logging_Disabled</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Event_Logging_Disabled_SEL_Full</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Event_Logging_Disabled_SEL_Almost_Full</code></dt>
<dd>Defaults to Warning.</dd></dl>
</dl>
<dt><code>IPMI_System_Event</code></dt>
<dd>The following states correspond to System Event sensors w/ System Event specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_System_Event_System_Reconfigured</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_System_Event_OEM_System_Boot_Event</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_Event_Undetermined_System_Hardware_Failure</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_System_Event_Entry_Added_To_Auxiliary_Log</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_Event_PEF_Action</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_Event_Timestamp_Clock_Sync</code></dt>
<dd>Defaults to Warning.</dd></dl>
</dl>
<dt><code>IPMI_Critical_Interrupt</code></dt>
<dd>The following states correspond to Critical Interrupt sensors w/ Critical Interrupt specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Critical_Interrupt_Front_Panel_NMI_Diagnostic_Interrupt</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Critical_Interrupt_Bus_Timeout</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Critical_Interrupt_I_O_Channel_Check_NMI</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Critical_Interrupt_Software_NMI</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Critical_Interrupt_PCI_PERR</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Critical_Interrupt_PCI_SERR</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Critical_Interrupt_EISA_Fail_Safe_Timeout</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Critical_Interrupt_Bus_Correctable_Error</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Critical_Interrupt_Bus_Uncorrectable_Error</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Critical_Interrupt_Fatal_NMI</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Critical_Interrupt_Bus_Fatal_Error</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Slot_Connector</code></dt>
<dd>The following states correspond to Slot Connector sensors w/ Slot Connector specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Slot_Connector_Fault_Status_Asserted</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Slot_Connector_Identify_Status_Asserted</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Slot_Connector_Slot_Connector_Device_Installed_Attached</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Slot_Connector_Slot_Connector_Ready_For_Device_Installation</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Slot_Connector_Slot_Connector_Ready_For_Device_Removal</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Slot_Connector_Slot_Power_Is_Off</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Slot_Connector_Slot_Connector_Device_Removal_Request</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Slot_Connector_Interlock_Asserted</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Slot_Connector_Slot_Is_Disabled</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Slot_Connector_Slot_Holds_Spare_Device</code></dt>
<dd>Defaults to Nominal.</dd></dl>
</dl>
<dt><code>IPMI_Watchdog2</code></dt>
<dd>The following states correspond to Watchdog 2 sensors w/ Watchdog 2 specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Watchdog2_Timer_Expired</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Watchdog2_Hard_Reset</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Watchdog2_Power_Down</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Watchdog2_Power_Cycle</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Watchdog2_Reserved1</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Watchdog2_Reserved2</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Watchdog2_Reserved3</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Watchdog2_Reserved4</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Watchdog2_Timer_Interrupt</code></dt>
<dd>Defaults to Warning.</dd></dl>
</dl>
<dt><code>IPMI_Entity_Presence</code></dt>
<dd>The following states correspond to Entity Presence sensors w/ Entity Presence specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Entity_Presence_Entity_Present</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Entity_Presence_Entity_Absent</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Entity_Presence_Entity_Disabled</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Management_Subsystem_Health</code></dt>
<dd>The following states correspond to Management Subsystem Health sensors w/ Management Subsystem Health specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Management_Subsystem_Health_Sensor_Access_Degraded_Or_Unavailable</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Management_Subsystem_Health_Controller_Access_Degraded_Or_Unavailable</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Management_Subsystem_Health_Management_Controller_Off_Line</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Management_Subsystem_Health_Management_Controller_Unavailable</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Management_Subsystem_Health_Sensor_Failure</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Management_Subsystem_Health_FRU_Failure</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Battery</code></dt>
<dd>The following states correspond to Battery sensors w/ Battery specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Battery_Battery_Low</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Battery_Battery_Failed</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Battery_Battery_Presence_Detected</code></dt>
<dd>Defaults to Nominal.</dd></dl>
</dl>
<dt><code>IPMI_FRU_State</code></dt>
<dd>The following states correspond to FRU State sensors w/ FRU State specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_FRU_State_FRU_Not_Installed</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_FRU_State_FRU_Inactive</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_FRU_State_FRU_Activation_Requested</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_FRU_State_FRU_Activation_In_Progress</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_FRU_State_FRU_Active</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_FRU_State_FRU_Deactivation_Requested</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_FRU_State_FRU_Deactivation_In_Progress</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_FRU_State_FRU_Communication_Lost</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Cable_Interconnect</code></dt>
<dd>The following states correspond to Cable/Interconnect sensors w/ Cable/Interconnect specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Cable_Interconnect_Is_Connected</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Cable_Interconnect_Incorrect_Cable_Connected_Incorrect_Interconnection</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
<dt><code>IPMI_Boot_Error</code></dt>
<dd>The following states correspond to Boot Error sensors w/ Boot Error specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Boot_Error_No_Bootable_Media</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Boot_Error_Non_Bootable_Diskette_Left_In_Drive</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Boot_Error_PXE_Server_Not_Found</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Boot_Error_Invalid_Boot_Sector</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_Boot_Error_Timeout_Waiting_For_User_Selection_Of_Boot_Source</code></dt>
<dd>Defaults to Warning.</dd></dl>
</dl>
<dt><code>IPMI_Button_Switch</code></dt>
<dd>The following states correspond to Button/Switch sensors w/ Button/Switch specific output states.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>IPMI_Button_Switch_Power_Button_Pressed</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Button_Switch_Sleep_Button_Pressed</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Button_Switch_Reset_Button_Pressed</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_Button_Switch_FRU_Latch_Open</code></dt>
<dd>Defaults to Warning.</dd>
<dt><code>IPMI_Button_Switch_FRU_Service_Request_Button</code></dt>
<dd>Defaults to Warning.</dd></dl>
</dl>
<dt><code>IPMI_System_ACPI_Power_State</code></dt>
<dd>
</dd><dl>
<dd>
</dd><dl>
<dt><code>IPMI_System_ACPI_Power_State_S0_G0</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_ACPI_Power_State_S1</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_ACPI_Power_State_S2</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_ACPI_Power_State_S3</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_ACPI_Power_State_S4</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_ACPI_Power_State_S5_G2</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_ACPI_Power_State_S4_S5_Soft_Off</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_ACPI_Power_State_G3_Mechanical_Off</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_ACPI_Power_State_Sleeping_in_an_S1_S2_or_S3_States</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_ACPI_Power_State_G1_Sleeping</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_ACPI_Power_State_S5_Entered_By_Override</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_ACPI_Power_State_Legacy_ON_State</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_ACPI_Power_State_Legacy_OFF_State</code></dt>
<dd>Defaults to Nominal.</dd>
<dt><code>IPMI_System_ACPI_Power_State_Unspecified</code></dt>
<dd>Defaults to Critical.</dd>
<dt><code>IPMI_System_ACPI_Power_State_Unknown</code></dt>
<dd>Defaults to Critical.</dd></dl>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/ipmi_monitoring_sensors.conf</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2003-2008 FreeIPMI Core Team. </p>
<p> FreeIPMI is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipmimonitoring/">ipmimonitoring</a>(8), <a href="/docs/linux/man/3-libipmimonitoring/">libipmimonitoring</a>(3) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
