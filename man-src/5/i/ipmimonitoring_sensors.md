---
title: "ipmimonitoring_sensors(5)"
name: "ipmimonitoring_sensors"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipmimonitoring_sensors/"
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
<dt><code>IPMI_Threshold_Sensor</code></p>
<dd>The following states correspond to threshold sensors. This normally applies to sensors that measure non-discrete values, such as temperatures, voltages, RPM, etc.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Threshold_Sensor_At_Or_Below_Lower_Non_Critical_Threshold</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Threshold_Sensor_At_Or_Below_Lower_Critical_Threshold</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Threshold_Sensor_At_Or_Below_Lower_Non_Recoverable_Threshold</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Threshold_Sensor_At_Or_Above_Upper_Non_Critical_Threshold</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Threshold_Sensor_At_Or_Above_Upper_Critical_Threshold</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Threshold_Sensor_At_Or_Above_Upper_Non_Recoverable_Threshold</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Voltage_State</code></p>
<dd>The following states correspond to Voltage sensors that report an assertion or deassertion.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Voltage_State_Deasserted</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Voltage_State_Asserted</code></p>
<dd>Defaults to Warning.</dl>
</dl>
<dt><code>IPMI_Voltage_Performance</code></p>
<dd>The following states correspond to Voltage sensors that report on performance.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Voltage_Performance_Met</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Voltage_Performance_Lags</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Fan_Device_Install</code></p>
<dd>The following states correspond to Fan sensors that report on device installation.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Fan_Device_Install_Device_Removed_Device_Absent</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Fan_Device_Install_Device_Inserted_Device_Present</code></p>
<dd>Defaults to Nominal.</dl>
</dl>
<dt><code>IPMI_Fan_Transition_Availability</code></p>
<dd>The following states correspond to Fan sensors that report on device availability.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Fan_Transition_Availability_To_Running</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Fan_Transition_Availability_To_In_Test</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Fan_Transition_Availability_To_Power_Off</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Fan_Transition_Availability_To_On_Line</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Fan_Transition_Availability_To_Off_Line</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Fan_Transition_Availability_To_Off_Duty</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Fan_Transition_Availability_To_Degraded</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Fan_Transition_Availability_To_Power_Save</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Fan_Transition_Availability_Install_Error</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Fan_Redundancy</code></p>
<dd>The following states correspond to Fan sensors that report on redundancy.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Fan_Redundancy_Fully_Redundant</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Fan_Redundancy_Redundancy_Lost</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Fan_Redundancy_Redundancy_Degraded</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Fan_Redundancy_Non_Redundant_Sufficient_Resources_From_Redundant</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Fan_Redundancy_Non_Redundant_Sufficient_Resources_From_Insufficient_Redundancy</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Fan_Redundancy_Non_Redundant_Insufficient_Resources</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Fan_Redundancy_Redundancy_Degraded_From_Fully_Redundant</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Fan_Redundancy_Redundancy_Degraded_From_Non_Redundant</code></p>
<dd>Defaults to Warning.</dl>
</dl>
<dt><code>IPMI_Processor_State</code></p>
<dd>The following states correspond to Processor sensors that report an assertion or deassertion.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Processor_State_Deasserted</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Processor_State_Asserted</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Power_Supply_State</code></p>
<dd>The following states correspond to Power_Supply sensors that report an assertion or deassertion.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Power_Supply_State_Deasserted</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Supply_State_Asserted</code></p>
<dd>Defaults to Nominal.</dl>
</dl>
<dt><code>IPMI_Power_Supply_Redundancy</code></p>
<dd>The following states correspond to Power Supply sensors that report on redundancy.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Power_Supply_Redundancy_Fully_Redundant</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Power_Supply_Redundancy_Redundancy_Lost</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Supply_Redundancy_Redundancy_Degraded</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Power_Supply_Redundancy_Non_Redundant_Sufficient_Resources_From_Redundant</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Supply_Redundancy_Non_Redundant_Sufficient_Resources_From_Insufficient_Redundancy</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Supply_Redundancy_Non_Redundant_Insufficient_Resources</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Supply_Redundancy_Redundancy_Degraded_From_Fully_Redundant</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Power_Supply_Redundancy_Redundancy_Degraded_From_Non_Redundant</code></p>
<dd>Defaults to Warning.</dl>
</dl>
<dt><code>IPMI_Power_Unit_Device_Install</code></p>
<dd>The following states correspond to Power Unit sensors that report on device installation.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Power_Unit_Device_Install_Device_Removed_Device_Absent</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Unit_Device_Install_Device_Inserted_Device_Present</code></p>
<dd>Defaults to Nominal.</dl>
</dl>
<dt><code>IPMI_Power_Unit_Redundancy</code></p>
<dd>The following states correspond to Power Unit sensors that report on redundancy.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Power_Unit_Redundancy_Fully_Redundant</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Power_Unit_Redundancy_Redundancy_Lost</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Unit_Redundancy_Redundancy_Degraded</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Power_Unit_Redundancy_Non_Redundant_Sufficient_Resources_From_Redundant</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Unit_Redundancy_Non_Redundant_Sufficient_Resources_From_Insufficient_Redundancy</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Unit_Redundancy_Non_Redundant_Insufficient_Resources</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Unit_Redundancy_Redundancy_Degraded_From_Fully_Redundant</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Power_Unit_Redundancy_Redundancy_Degraded_From_Non_Redundant</code></p>
<dd>Defaults to Warning.</dl>
</dl>
<dt><code>IPMI_Module_Board_State</code></p>
<dd>The following states correspond to Module/Board sensors that report an assertion or deassertion.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Module_Board_State_Deasserted</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Module_Board_State_Asserted</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Module_Board_Device_Install</code></p>
<dd>The following states correspond to Module/Board sensors that report on device installation.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Module_Board_Device_Install_Device_Removed_Device_Absent</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Module_Board_Device_Install_Device_Inserted_Device_Present</code></p>
<dd>Defaults to Nominal.</dl>
</dl>
<dt><code>IPMI_Drive_Slot_State</code></p>
<dd>The following states correspond to Drive Slot sensors that report an assertion or deassertion.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Drive_Slot_State_Deasserted</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Drive_Slot_State_Asserted</code></p>
<dd>Defaults to Nominal.</dl>
</dl>
<dt><code>IPMI_Drive_Slot_Predictive_Failure</code></p>
<dd>The following states correspond to Drive_Slot sensors that report a predictive failure assertion or deassertion.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Drive_Slot_Predictive_Failure_Deasserted</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Drive_Slot_Predictive_Failure_Asserted</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Drive_Slot_Device_Install</code></p>
<dd>The following states correspond to Drive Slot sensors that report on device installation.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Drive_Slot_Device_Install_Device_Removed_Device_Absent</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Drive_Slot_Device_Install_Device_Inserted_Device_Present</code></p>
<dd>Defaults to Nominal.</dl>
</dl>
<dt><code>IPMI_Button_Switch_State</code></p>
<dd>The following states correspond to Button/Switch sensors that report an assertion or deassertion.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Button_Switch_State_Deasserted</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Button_Switch_State_Asserted</code></p>
<dd>Defaults to Nominal.</dl>
</dl>
<dt><code>IPMI_Entity_Presence_Device_Install</code></p>
<dd>The following states correspond to Entity Presence sensors that report on device installation.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Entity_Presence_Device_Install_Device_Removed_Device_Absent</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Entity_Presence_Device_Install_Device_Inserted_Device_Present</code></p>
<dd>Defaults to Nominal.</dl>
</dl>
<dt><code>IPMI_Physical_Security</code></p>
<dd>The following states correspond to Physical Security sensors w/ Physical Security specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Physical_Security_General_Chassis_Intrusion</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Physical_Security_Drive_Bay_Intrusion</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Physical_Security_IO_Card_Intrusion</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Physical_Security_Processor_Area_Intrusion</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Physical_Security_LAN_Leash_Lost</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Physical_Security_Unauthorized_Dock_Undock</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Physical_Security_FAN_Area_Intrusion</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Platform_Security_Violation_Attempt</code></p>
<dd>The following states correspond to Platform Violation Attempt sensors w/ Platform Security Violation Attempt specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Platform_Security_Violation_Attempt_Secure_Mode_Violation_Attempt</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Platform_Security_Violation_Attempt_Pre_Boot_Password_Violation_User_Password</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Platform_Security_Violation_Attempt_Pre_Boot_Password_Violation_Setup_Password</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Platform_Security_Violation_Attempt_Pre_Boot_Password_Violation_Network_Boot_Password</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Platform_Security_Violation_Attempt_Other_Pre_Boot_Password_Violation</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Platform_Security_Violation_Attempt_Out_Of_Band_Access_Password_Violation</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Processor</code></p>
<dd>The following states correspond to Processor sensors w/ Processor specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Processor_IERR</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Processor_Thermal_Trip</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Processor_FRB1_BIST_Failure</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Processor_FRB2_Hang_In_POST_Failure</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Processor_FRB3_Processor_Startup_Initialization_Failure</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Processor_Configuration_Error</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Processor_SMBIOS_Uncorrectable_CPU_Complex_Error</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Processor_Processor_Presence_Detected</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Processor_Processor_Disabled</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Processor_Terminator_Presence_Detected</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Processor_Processor_Automatically_Throttled</code></p>
<dd>Defaults to Warning.</dl>
</dl>
<dt><code>IPMI_Power_Supply</code></p>
<dd>The following states correspond to Power Supply sensors w/ Power Supply specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Power_Supply_Presence_Detected</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Power_Supply_Power_Supply_Failure_Detected</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Supply_Predictive_Failure</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Supply_Power_Supply_Input_Lost_AC_DC</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Supply_Power_Supply_Input_Lost_Or_Out_Of_Range</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Supply_Power_Supply_Input_Out_Of_Range_But_Present</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Supply_Configuration_Error</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Power_Unit</code></p>
<dd>The following states correspond to Power Unit sensors w/ Power Unit specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Power_Unit_Power_Off_Power_Down</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Power_Unit_Power_Cycle</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Power_Unit_240VA_Power_Down</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Power_Unit_Interlock_Power_Down</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Power_Unit_AC_Lost</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Unit_Soft_Power_Control_Failure</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Unit_Power_Unit_Failure_Detected</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Power_Unit_Predictive_Failure</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Memory</code></p>
<dd>The following states correspond to Memory sensors w/ Memory specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Memory_Correctable_ECC_Memory_Error</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Memory_Uncorrectable_ECC_Memory_Error</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Memory_Parity</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Memory_Memory_Scrub_Failed</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Memory_Memory_Device_Disabled</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Memory_Correctable_ECC_Memory_Error_Logging_Limit_Reached</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Memory_Presence_Detected</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Memory_Configuration_Error</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Memory_Spare</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Memory_Memory_Automatically_Throttled</code></p>
<dd>Defaults to Warning.</dl>
</dl>
<dt><code>IPMI_Drive_Slot</code></p>
<dd>The following states correspond to Drive Slot sensors w/ Drive Slot specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Drive_Slot_Drive_Presence</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Drive_Slot_Drive_Fault</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Drive_Slot_Predictive_Failure</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Drive_Slot_Hot_Spare</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Drive_Slot_Consistency_Check_Parity_Check_In_Progress</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Drive_Slot_In_Critical_Array</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Drive_Slot_In_Failed_Array</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Drive_Slot_Rebuild_Remap_In_Progress</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Drive_Slot_Rebuild_Remap_Aborted</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_System_Firmware_Progress</code></p>
<dd>The following states correspond to System Firmware Progress sensors w/ System Firmware Progress specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_System_Firmware_Progress_System_Firmware_Error</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_System_Firmware_Progress_System_Firmware_Hang</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_System_Firmware_Progress_System_Firmware_Progress</code></p>
<dd>Defaults to Nominal.</dl>
</dl>
<dt><code>IPMI_Event_Logging_Disabled</code></p>
<dd>The following states correspond to Event Logging Disabled sensors w/</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Event_Logging_Disabled_Correctable_Memory_Logging_Disabled</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Event_Logging_Disabled_Event_Type_Logging_Disabled</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Event_Logging_Disabled_Log_Area_Reset_Cleared</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Event_Logging_Disabled_All_Event_Logging_Disabled</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Event_Logging_Disabled_SEL_Full</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Event_Logging_Disabled_SEL_Almost_Full</code></p>
<dd>Defaults to Warning.</dl>
</dl>
<dt><code>IPMI_System_Event</code></p>
<dd>The following states correspond to System Event sensors w/ System Event specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_System_Event_System_Reconfigured</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_System_Event_OEM_System_Boot_Event</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_Event_Undetermined_System_Hardware_Failure</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_System_Event_Entry_Added_To_Auxiliary_Log</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_Event_PEF_Action</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_Event_Timestamp_Clock_Sync</code></p>
<dd>Defaults to Warning.</dl>
</dl>
<dt><code>IPMI_Critical_Interrupt</code></p>
<dd>The following states correspond to Critical Interrupt sensors w/ Critical Interrupt specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Critical_Interrupt_Front_Panel_NMI_Diagnostic_Interrupt</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Critical_Interrupt_Bus_Timeout</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Critical_Interrupt_I_O_Channel_Check_NMI</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Critical_Interrupt_Software_NMI</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Critical_Interrupt_PCI_PERR</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Critical_Interrupt_PCI_SERR</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Critical_Interrupt_EISA_Fail_Safe_Timeout</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Critical_Interrupt_Bus_Correctable_Error</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Critical_Interrupt_Bus_Uncorrectable_Error</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Critical_Interrupt_Fatal_NMI</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Critical_Interrupt_Bus_Fatal_Error</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Slot_Connector</code></p>
<dd>The following states correspond to Slot Connector sensors w/ Slot Connector specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Slot_Connector_Fault_Status_Asserted</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Slot_Connector_Identify_Status_Asserted</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Slot_Connector_Slot_Connector_Device_Installed_Attached</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Slot_Connector_Slot_Connector_Ready_For_Device_Installation</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Slot_Connector_Slot_Connector_Ready_For_Device_Removal</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Slot_Connector_Slot_Power_Is_Off</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Slot_Connector_Slot_Connector_Device_Removal_Request</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Slot_Connector_Interlock_Asserted</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Slot_Connector_Slot_Is_Disabled</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Slot_Connector_Slot_Holds_Spare_Device</code></p>
<dd>Defaults to Nominal.</dl>
</dl>
<dt><code>IPMI_Watchdog2</code></p>
<dd>The following states correspond to Watchdog 2 sensors w/ Watchdog 2 specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Watchdog2_Timer_Expired</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Watchdog2_Hard_Reset</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Watchdog2_Power_Down</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Watchdog2_Power_Cycle</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Watchdog2_Reserved1</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Watchdog2_Reserved2</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Watchdog2_Reserved3</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Watchdog2_Reserved4</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Watchdog2_Timer_Interrupt</code></p>
<dd>Defaults to Warning.</dl>
</dl>
<dt><code>IPMI_Entity_Presence</code></p>
<dd>The following states correspond to Entity Presence sensors w/ Entity Presence specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Entity_Presence_Entity_Present</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Entity_Presence_Entity_Absent</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Entity_Presence_Entity_Disabled</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Management_Subsystem_Health</code></p>
<dd>The following states correspond to Management Subsystem Health sensors w/ Management Subsystem Health specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Management_Subsystem_Health_Sensor_Access_Degraded_Or_Unavailable</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Management_Subsystem_Health_Controller_Access_Degraded_Or_Unavailable</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Management_Subsystem_Health_Management_Controller_Off_Line</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Management_Subsystem_Health_Management_Controller_Unavailable</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Management_Subsystem_Health_Sensor_Failure</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Management_Subsystem_Health_FRU_Failure</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Battery</code></p>
<dd>The following states correspond to Battery sensors w/ Battery specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Battery_Battery_Low</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Battery_Battery_Failed</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Battery_Battery_Presence_Detected</code></p>
<dd>Defaults to Nominal.</dl>
</dl>
<dt><code>IPMI_FRU_State</code></p>
<dd>The following states correspond to FRU State sensors w/ FRU State specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_FRU_State_FRU_Not_Installed</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_FRU_State_FRU_Inactive</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_FRU_State_FRU_Activation_Requested</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_FRU_State_FRU_Activation_In_Progress</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_FRU_State_FRU_Active</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_FRU_State_FRU_Deactivation_Requested</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_FRU_State_FRU_Deactivation_In_Progress</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_FRU_State_FRU_Communication_Lost</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Cable_Interconnect</code></p>
<dd>The following states correspond to Cable/Interconnect sensors w/ Cable/Interconnect specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Cable_Interconnect_Is_Connected</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Cable_Interconnect_Incorrect_Cable_Connected_Incorrect_Interconnection</code></p>
<dd>Defaults to Critical.</dl>
</dl>
<dt><code>IPMI_Boot_Error</code></p>
<dd>The following states correspond to Boot Error sensors w/ Boot Error specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Boot_Error_No_Bootable_Media</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Boot_Error_Non_Bootable_Diskette_Left_In_Drive</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Boot_Error_PXE_Server_Not_Found</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Boot_Error_Invalid_Boot_Sector</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_Boot_Error_Timeout_Waiting_For_User_Selection_Of_Boot_Source</code></p>
<dd>Defaults to Warning.</dl>
</dl>
<dt><code>IPMI_Button_Switch</code></p>
<dd>The following states correspond to Button/Switch sensors w/ Button/Switch specific output states.</p>
<dl>
<dd>
<dl>
<dt><code>IPMI_Button_Switch_Power_Button_Pressed</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Button_Switch_Sleep_Button_Pressed</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Button_Switch_Reset_Button_Pressed</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_Button_Switch_FRU_Latch_Open</code></p>
<dd>Defaults to Warning.</p>
<dt><code>IPMI_Button_Switch_FRU_Service_Request_Button</code></p>
<dd>Defaults to Warning.</dl>
</dl>
<dt><code>IPMI_System_ACPI_Power_State</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>IPMI_System_ACPI_Power_State_S0_G0</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_ACPI_Power_State_S1</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_ACPI_Power_State_S2</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_ACPI_Power_State_S3</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_ACPI_Power_State_S4</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_ACPI_Power_State_S5_G2</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_ACPI_Power_State_S4_S5_Soft_Off</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_ACPI_Power_State_G3_Mechanical_Off</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_ACPI_Power_State_Sleeping_in_an_S1_S2_or_S3_States</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_ACPI_Power_State_G1_Sleeping</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_ACPI_Power_State_S5_Entered_By_Override</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_ACPI_Power_State_Legacy_ON_State</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_ACPI_Power_State_Legacy_OFF_State</code></p>
<dd>Defaults to Nominal.</p>
<dt><code>IPMI_System_ACPI_Power_State_Unspecified</code></p>
<dd>Defaults to Critical.</p>
<dt><code>IPMI_System_ACPI_Power_State_Unknown</code></p>
<dd>Defaults to Critical.</dl>
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
