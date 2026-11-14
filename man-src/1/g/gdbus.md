---
title: "gdbus(1)"
name: "gdbus"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdbus/"
description: "gdbus – Tool for working with D-Bus objects"
---

<h2 class="name">NAME</h2>
<p> gdbus &#8211; Tool for working with D-Bus objects </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gdbus</code> introspect [&#8211;system | &#8211;session | &#8211;address&nbsp;<i>address</i>] &#8211;dest&nbsp;<i>bus_name</i> &#8211;object-path&nbsp;<i>/path/to/object</i> [&#8211;xml] [&#8211;recurse] [&#8211;only-properties]</p>
<dt> <code>gdbus</code> monitor [&#8211;system | &#8211;session | &#8211;address&nbsp;<i>address</i>] &#8211;dest&nbsp;<i>bus_name</i> [&#8211;object-path&nbsp;<i>/path/to/object</i>]</p>
<dt> <code>gdbus</code> call [&#8211;system | &#8211;session | &#8211;address&nbsp;<i>address</i>] &#8211;dest&nbsp;<i>bus_name</i> &#8211;object-path&nbsp;<i>/path/to/object</i> &#8211;method&nbsp;<i>org.project.InterfaceName.MethodName</i> [&#8211;timeout&nbsp;<i>seconds</i> | &#8211;interactive] ARG1 ARG2&#8230;</p>
<dt> <code>gdbus</code> emit [&#8211;system | &#8211;session | &#8211;address&nbsp;<i>address</i>] &#8211;object-path&nbsp;<i>/path/to/object</i> &#8211;signal&nbsp;<i>org.project.InterfaceName.SignalName</i> [&#8211;dest&nbsp;<i>unique_bus_name</i>] ARG1 ARG2&#8230;</p>
<dt> <code>gdbus</code> wait [&#8211;system | &#8211;session | &#8211;address&nbsp;<i>address</i>] &#8211;activate&nbsp;<i>bus_name</i> [&#8211;timeout&nbsp;<i>seconds</i>] <i>bus_name</i></p>
<dt> <code>gdbus</code> help</dl>
<h2>DESCRIPTION</h2>
<p> <code>gdbus</code></p>
<dd>is a simple tool for working with D-Bus objects.</p>
<h2>COMMANDS</h2>
<p> <code>introspect</code></p>
<dl>
<dt>
<dd> Prints out interfaces and property values for a remote object. For this to work, the owner of the object needs to implement the org.freedesktop.DBus.Introspectable interface. If the <code>&#8211;xml</code> option is used, the returned introspection XML is printed, otherwise a parsed pretty representation is printed. The <code>&#8211;recurse</code> option can be used to introspect children (and their children and so on) and the <code>&#8211;only-properties</code> option can be used to only print the interfaces with properties.</dl>
<p> <code>monitor</code></p>
<dl>
<dt>
<dd> Monitors one or all objects owned by the owner of <i>bus_name</i>.</dl>
<p> <code>call</code></p>
<dl>
<dt>
<dd> Invokes a method on a remote object. Each argument to pass to the method must be specified as a serialized <code>GVariant</code> except that strings do not need explicit quotes. The return values are printed out as serialized <code>GVariant</code> values.</dl>
<p> <code>emit</code></p>
<dl>
<dt>
<dd> Emits a signal. Each argument to include in the signal must be specified as a serialized <code>GVariant</code> except that strings do not need explicit quotes.</dl>
<p> <code>wait</code></p>
<dl>
<dt>
<dd> Waits until <i>bus_name</i> is owned by some process on the bus. If the <code>&#8211;activate</code> is specified, that bus name will be auto-started first. It may be the same as the bus name being waited for, or different.</dl>
<p> <code>help</code></p>
<dl>
<dt>
<dd> Prints help and exit.</dl>
<h2>BASH COMPLETION</h2>
<p> <code>gdbus</code> ships with a bash completion script to complete commands, destinations, bus names, object paths and interface/method names.</p>
<h2>EXAMPLES</h2>
<p>&nbsp;<wbr>&nbsp;This shows how to introspect an object &#8211; note that the value of each<br />
&nbsp;<wbr>&nbsp;property is displayed: </p>
<dl>
<dt>
<dd>
<pre><code>
$ gdbus introspect-- system-- dest org.freedesktop.NetworkManager-- object - path / org / freedesktop / NetworkManager / Devices / 0 node / org / freedesktop / NetworkManager / Devices / 0
{
    interface org.freedesktop.DBus.Introspectable
    {
    methods:
        Introspect(out s data);
    };
    interface org.freedesktop.DBus.Properties
    {
    methods:
        Get(in s interface,
            in s propname,
            out v value);
        Set(in s interface,
            in s propname,
            in v value);
        GetAll(in s interface,
               out a{sv} props);
    };
    interface org.freedesktop.NetworkManager.Device.Wired
    {
      signals:
        PropertiesChanged(a{sv} arg_0);
    properties:
        readonly b Carrier = false;
        readonly u Speed = 0;
        readonly s HwAddress = '00:1D:72:88:BE:97';
    };
    interface org.freedesktop.NetworkManager.Device
    {
    methods:
        Disconnect();
      signals:
        StateChanged(u arg_0,
                     u arg_1,
                     u arg_2);
    properties:
        readonly u DeviceType = 1;
        readonly b Managed = true;
        readwrite o Ip6Config = '/';
        readwrite o Dhcp4Config = '/';
        readwrite o Ip4Config = '/';
        readonly u State = 2;
        readwrite u Ip4Address = 0;
        readonly u Capabilities = 3;
        readonly s Driver = 'e1000e';
        readwrite s Interface = 'eth0';
        readonly s Udi = '/sys/devices/pci0000:00/0000:00:19.0/net/eth0';
    };
};
</code></pre>
</dl>
<p> The <code>&#8211;recurse</code> and <code>&#8211;only-properties</code> options can be useful when wanting to inspect all objects owned by a particular process: </p>
<dl>
<dt>
<dd>
$ gdbus introspect&#8211; system&#8211; dest org.freedesktop.UPower&#8211; object &#8211; path / &#8211;recurse&#8211; only &#8211; properties node /<br />
{<br />
    node / org<br />
    {<br />
        node / org / freedesktop<br />
        {<br />
            node / org / freedesktop / UPower<br />
            {<br />
                interface org.freedesktop.UPower<br />
                {<br />
                properties:<br />
                    readonly b IsDocked = true;<br />
                    readonly b LidForceSleep = false;<br />
                    readonly b LidIsPresent = false;<br />
                    readonly b LidIsClosed = false;<br />
                    readonly b OnLowBattery = false;<br />
                    readonly b OnBattery = false;<br />
                    readonly b CanHibernate = true;<br />
                    readonly b CanSuspend = true;<br />
                    readonly s DaemonVersion = &#8216;0.9.10&#8217;;<br />
                };<br />
                node / org / freedesktop / UPower / Policy{};<br />
                node / org / freedesktop / UPower / Wakeups<br />
                {<br />
                    interface org.freedesktop.UPower.Wakeups<br />
                    {<br />
                    properties:<br />
                        readonly b HasCapability = true;<br />
                    };<br />
                };<br />
            };<br />
        };<br />
    };<br />
};
</dl>
<p> In a similar fashion, the <code>introspect</code> command can be used to learn details about the Notify method: </p>
<dl>
<dt>
<dd>
[&#8230;] interface org.freedesktop.Notifications<br />
{<br />
methods:<br />
    GetServerInformation(out s return_name,<br />
                         out s return_vendor,<br />
                         out s return_version,<br />
                         out s return_spec_version);<br />
    GetCapabilities(out as return_caps);<br />
    CloseNotification(in u id);<br />
    Notify(in s app_name,<br />
           in u id,<br />
           in s icon,<br />
           in s summary,<br />
           in s body,<br />
           in as actions,<br />
           in a{sv} hints,<br />
           in i timeout,<br />
           out u return_id);<br />
};<br />
[&#8230;]
</dl>
<p> With this information, it&#8217;s easy to use the <code>call</code> command to display a notification </p>
<dl>
<dt>
<dd>
$ gdbus call&#8211; session&#8211; dest org.freedesktop.Notifications&#8211; object &#8211; path / org / freedesktop / Notifications&#8211; method org.freedesktop.Notifications.Notify my_app_name 42 gtk &#8211; dialog &#8211; info &#8220;The Summary&#8221;<br />
                                                                                                                                                                                                 &#8220;Here&#8217;s the body of the notification&#8221; [] {} 5000(uint32 12, )
</dl>
<p> Call a method with file handle argument: </p>
<dl>
<dt>
<dd>
$ gdbus call&#8211; session&#8211; dest org.example.foo&#8211; object &#8211; path / org / example / foo&#8211; method SendFDs 1 10 10 &lt; file.foo
</dl>
<p> Monitoring all objects on a service: </p>
<dl>
<dt>
<dd>
<pre>
$ gdbus monitor --system --dest org.freedesktop.ConsoleKit
Monitoring signals from all objects owned by org.freedesktop.ConsoleKit
The name org.freedesktop.ConsoleKit is owned by :1.15
/org/freedesktop/ConsoleKit/Session2: org.freedesktop.ConsoleKit.Session.ActiveChanged (false,)
/org/freedesktop/ConsoleKit/Seat1: org.freedesktop.ConsoleKit.Seat.ActiveSessionChanged ('',)
/org/freedesktop/ConsoleKit/Session2: org.freedesktop.ConsoleKit.Session.ActiveChanged (true,)
/org/freedesktop/ConsoleKit/Seat1: org.freedesktop.ConsoleKit.Seat.ActiveSessionChanged ('/org/freedesktop/ConsoleKit/Session2',)
</pre>
</dl>
<p> Monitoring a single object on a service: </p>
<dl>
<dt>
<dd>
$ gdbus monitor&#8211; system&#8211; dest org.freedesktop.NetworkManager&#8211; object &#8211; path / org / freedesktop / NetworkManager / AccessPoint / 4141 Monitoring signals on object / org / freedesktop / NetworkManager / AccessPoint / 4141 owned by org.freedesktop.NetworkManager The name org.freedesktop.NetworkManager is owned by : 1.5 / org / freedesktop / NetworkManager / AccessPoint / 4141 : org.freedesktop.NetworkManager.AccessPoint.PropertiesChanged({&#8216;Strength&#8217; : &lt;byte 0x5c&gt;}, ) / org / freedesktop / NetworkManager / AccessPoint / 4141 : org.freedesktop.NetworkManager.AccessPoint.PropertiesChanged({&#8216;Strength&#8217; : &lt;byte 0x64&gt;}, ) / org / freedesktop / NetworkManager / AccessPoint / 4141 : org.freedesktop.NetworkManager.AccessPoint.PropertiesChanged({&#8216;Strength&#8217; : &lt;byte 0x5e&gt;}, ) / org / freedesktop / NetworkManager / AccessPoint / 4141 : org.freedesktop.NetworkManager.AccessPoint.PropertiesChanged({&#8216;Strength&#8217; : &lt;byte 0x64&gt;}, )
</dl>
<p> Emitting a signal: </p>
<dl>
<dt>
<dd>
$ gdbus emit&#8211; session&#8211; object &#8211; path / foo&#8211; signal org.bar.Foo &#8220;[&#8216;foo&#8217;, &#8216;bar&#8217;, &#8216;baz&#8217;]&#8221;
</dl>
<p> Emitting a signal to a specific process: </p>
<dl>
<dt>
<dd>
<pre><code>
$ gdbus emit-- session-- object - path / bar-- signal org.bar.Bar someString-- dest : 1.42
</code></pre>
</dl>
<p> Waiting for a well-known name to be owned on the bus; this will <i>not</i> auto-start the service: </p>
<dl>
<dt>
<dd>
<pre>
$ gdbus wait --session org.bar.SomeName
</pre>
</dl>
<p> Auto-starting then waiting for a well-known name to be owned on the bus: </p>
<dl>
<dt>
<dd>
<pre>
$ gdbus wait --session --activate org.bar.SomeName
</pre>
</dl>
<p> Auto-starting a different service, then waiting for a well-known name to be owned on the bus. This is useful in situations where <i>SomeName</i> is not directly activatable: </p>
<dl>
<dt>
<dd>
<pre>
$ gdbus wait --session --activate org.bar.PrerequisiteName org.bar.SomeName
</pre>
</dl>
<p> Waiting for a well-known name and giving up after 30 seconds. By default, the timeout is disabled; or set <code>&#8211;timeout</code> to 0 to disable it: </p>
<dl>
<dt>
<dd>
<pre>
$ gdbus wait --session --timeout 30 org.bar.SomeName
</pre>
</dl>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://gitlab.gnome.org/GNOME/glib/issues/new">https://gitlab.gnome.org/GNOME/glib/issues/new</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dbus-send/">dbus-send</a></code>(1) </p>
<h2>Index</h2>
