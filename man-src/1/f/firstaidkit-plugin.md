---
title: "firstaidkit-plugin(1)"
name: "firstaidkit-plugin"
section: "1"
letter: "f"
url: "/docs/linux/man/1-firstaidkit-plugin/"
---

<h2>NAME firstaidkit-plugins</h2>
<p> <code>.SH</code>DESCRIPTION This man page tries to describe the inner workings of the plugin system for FirstAidKit. It also contains useful information to develop a plugin for firstaidkit. </p>
<h2>Plugin Suffixes</h2>
<p> All plugins belong to configured plugin directory. Recognized suffixes are: .py, .pyc, placed in a default location (/usr/{lib,lib64}/firstaidkit-plugins). </p>
<h2>Plugin Model</h2>
<p> The building blocks of the plugins are functions and flows. A function is a certain action that is taken inside the plugin. This action is more or less independent from the rest of the plugin actions. Things like fix, backup, restore&#8230; qualify as actions/functions. This does not mean that functions do not relate to each other. They are related by using the flow data structure (The data structure used for the flows is a dictionary). </p>
<p> A flow is the organization of functions in a directional graph that defines the &quot;flow&quot; of functions. Understand flow here as the order in which functions are executed when the plugin is used. This order/flow is specified using the function names, their return codes and the flow data structure. All this is contained within a dictionary (The Examples Sections shows how this is done.) </p>
<h2>Coding a Plugin</h2>
<dl>
<dt>1. Class methods and class attributes:</p>
<dd> The main plugin class has some class methods and some class attributes. These elements are used to describe the plugin and are used without actually using a instance of the plugin. This is important because we do not want to execute the __init__ function and cause lots of unnecessary stuff to go into memory when we are querying for plugin basic information. </p>
<p> The class attributes are: name, version, author and the defined flows. For the information to be displayed correctly to the user the plugin developer must include at least name, version and author as class attributes. The flows attribute is not necesarry if custom flows aren&#8217;t present. If the plugin developer is planning to create a custom flows he must declare the flows dictionary for your plugin. More information of the class attributes in the &quot;Class Attribute&quot; section. </p>
<p> The class methods are: info() (returns the name, version and author in a tuple), getDeps() (returns list of required flags for automated mode) and getFlows() (returns a list of possible flow names that the plugin can execute). The plugin developer doesn&#8217;t really have to worry about the methods as they are defined in the father class Plugin. Section &quot;Class Methods&quot; gives more infor on each one. </p>
<dt>2. Plugin dependencies</p>
<dd> You can also specify flags, which are required to be satisfied before the automated mode can use this plugin. The requirements should be returned as python set of strings by the getDeps() class method. Setting flags is also easy. Just use the provide() method common to all plugins. </p>
<p> There is also getConflicts() method, with the very same behaviour as getDeps(), but with the opposite meaning. Meaning, it is a set of flags, which have to NOT be satisfied for the plugin to be processed. </p>
<dt>3. Default functions:</p>
<dd> See section &quot;Common stuff for plugins&quot; </p>
<dt>4. Flows:</p>
<dd> There are two basic flows hardcoded into the system. These flows may *not* be used by plugin developers. The first flow is called diagnose: the intention with this flow is to give the user information of the state of the system that the plugin is analysing. This flow is intended to give general information and needs to be very fast. If the plugin needs to do some more detailed diagnose analysis, we suggest to create another flow called &#8216;detailedAnalysis&#8217;. When coding the diagnose flow, remember that it will be executed when the user asks for the information of *all* the plugins. The diagnose flow calls only the prepare, diagnose and clean tasks. The second flow is called fix: the intention with this flow is to actually fix whatever is wrong with the system. We suggest this flow to be as thorough as it needs to be. If there is more than one way to fix the problem, this flow would be the easiest one (the plugin developer can create other flow for the more complex ones). For this flow to be successfull the prepare, diagnose, backup, fix, restore and clean tasks must be present in the plugin. for more info see section &quot;Common stuff for plugins&quot;. Finally, to add a custom flow the plugin developer must initialize a dictionary named flows using flows = Flow.init(parent class) and fill it with the custom flows. For more info on adding flows see the &quot;Examples&quot; section. </p>
<dt>5. self._result and self._state</p>
<dd> These are the two variables that define the location of the plugin inside the flow dictionary. In each function, after it has done its intended action, the self._result variable must be changed to a correct value. Think of the self._result as the return value of each task. Before any task is executed, the self._result is set to None, so we can handle exceptions as special direction in flows. The self._result usually takes a firstaidkit return value (classes that define the return value). </p>
<p> Firstaidkit comes with predifined return value classes but the plugin developer may define his own return classes. One reason to define a custom return class is to have actual values be passed between tasks (this is not yet implemented as the tasks are in the same class and can interchange values using the class variable). The self._state is the name of the task where the plugin is at a certain moment. The self._state variable is of no real use to the plugin developer as he must know in what task the plugin is in. </p>
<dt>6. get_plugin()</p>
<dd> Each plugin must define a get_plugin function. This function must return the main class of the plugin. This is used to take out info from the plugin, and to instantiate it. If in doubt, take a look at the sample plugins that come with the man FirstAidKit code base. They can give you a pretty good idea of what to do when using a module, file &#8230; </p>
<dt>7. return values:</p>
<dd> For each function you code in a plugin you must use predefined return classes. It is necessary to have the extra wrapper because the python native types can get messy (1==True). Just use the ones provided by the plugin system, or create your own. </p>
</dl>
<h2>Common stuff</h2>
<p> Each plugin, by default, should exports some steps. The mandatory ones are:</p>
<dl>
<dt>prepare</p>
<dd> Initialize plugin, get environment.</p>
<dt>backup</p>
<dd> Backup everything we could touch in this plugin. (Also see the firstaidkit-backup manpage)</p>
<dt>diagnose</p>
<dd> Get info about the investigated system and determine where the problems are.</p>
<dt>fix</p>
<dd> Auto fix the errors from diagnose step.</p>
<dt>restore</p>
<dd> Restore system from backup.</p>
<dt>clean</p>
<dd> Destroy the plugin, cleanup.</dl>
<p> The plugin should ensure that the calling order is correct and the system cannot end in some indeterminate state. </p>
<h2>Python Modules:</h2>
<p> A plugin for the FirstAidKit must inherit from the pyfirstaidkit.Plugin class. It must also implement the mandatory plugin steps. The pyfirstaidkit.Plugin parent will provide a default flow that will use the functions defined by the plugin developer. Moreover, for the mandatory steps, the plugin developer must guarantee that the function will return a valid return class (see &quot;Return Values section&quot;). In other words, the function must return one of the possible return classes included in the default flow. Each plugin must have the get_plugin method in order to actually be seen by the firstaidkit backend. </p>
<h2>Class Attributes:</h2>
<p> This is how the diagnose and fix flows are coded in the backend plugin system.<br />
&nbsp;<wbr>flows[&quot;diagnose&quot;]&nbsp;<wbr>=&nbsp;<wbr>Flow({<br />
initial&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>{Return:&nbsp;<wbr>&quot;prepare&quot;},<br />
&quot;prepare&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>{ReturnSuccess:&nbsp;<wbr>&quot;diagnose&quot;, None:&nbsp;<wbr>&quot;clean&quot;},<br />
&quot;diagnose&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>{ReturnSuccess:&nbsp;<wbr>&quot;clean&quot;, ReturnFailure:&nbsp;<wbr>&quot;clean&quot;, None:&nbsp;<wbr>&quot;clean&quot;},<br />
&quot;clean&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>{ReturnSuccess: final, ReturnFailure: final, None: final}<br />
}, description=&quot;The default, fully automated, diagnose sequence&quot;) </p>
<p>&nbsp;<wbr>flows[&quot;fix&quot;]&nbsp;<wbr>=&nbsp;<wbr>Flow({<br />
initial&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>{Return:&nbsp;<wbr>&quot;prepare&quot;},<br />
&quot;prepare&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>{ReturnSuccess:&nbsp;<wbr>&quot;diagnose&quot;, None:&nbsp;<wbr>&quot;clean&quot;},<br />
&quot;diagnose&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>{ReturnSuccess:&nbsp;<wbr>&quot;clean&quot;, ReturnFailure:&nbsp;<wbr>&quot;backup&quot;, None:&nbsp;<wbr>&quot;clean&quot;},<br />
&quot;backup&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>{ReturnSuccess:&nbsp;<wbr>&quot;fix&quot;, ReturnFailure:&nbsp;<wbr>&quot;clean&quot;, None:&nbsp;<wbr>&quot;clean&quot;},<br />
&quot;fix&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>{ReturnSuccess:&nbsp;<wbr>&quot;clean&quot;, ReturnFailure:&nbsp;<wbr>&quot;restore&quot;, None:&nbsp;<wbr>&quot;restore&quot;},<br />
&quot;restore&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>{ReturnSuccess:&nbsp;<wbr>&quot;clean&quot;, ReturnFailure:&nbsp;<wbr>&quot;clean&quot;, None:&nbsp;<wbr>&quot;clean&quot;},<br />
&quot;clean&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>{ReturnSuccess: final, ReturnFailure: final, None: final}<br />
}, description=&quot;The default, fully automated, fixing sequence&quot;) </p>
<p> Other important class attributes are: name, version, author and description. They are selfexplanatory. </p>
<h2>Class Methods:</h2>
<p> pyfirstaidkit.Plugin defines:</p>
<dl>
<dt>nextstep()</p>
<dd> This is used to return the next function that should be executed. __iter__() is not used because there is no control over __iter__() in an iteration. nextstep() allows us execution of the flow without the need for an iteration. However the iteration is present in the class and can be used accordingly.</p>
<dt>__iter__() and next()</p>
<dd> Iterator protocol, works in the same way as nextstep() but end with StopIteration exception</p>
<dt>actions()</p>
<dd> Returns list of available step names</p>
<dt>call(step)</p>
<dd> Calls one specific step identified by name</p>
<dt>info()</p>
<dd> Returns tuple of strings defined as (name of plugin, version, author)</p>
<dt>changeFlow()</p>
<dd> Allows the caller to change to some other flow defined in the plugin.</p>
<dt>getFlows()</p>
<dd> Returns all the possible flows that the plugin supports. And of course the steps itself. They are defined as methods with the same names as used in actions().</p>
<dt>getDeps()</p>
<dd> Returns list of flags which are required for this plugin to operate in automated mode.</p>
<dt>provide(flag)</p>
<dd> Adds flag into the pool of satisfied flags.</p>
<dt>require(flag)</p>
<dd> Queries the state of flag. Returns True if set, False otherwise. </p>
</dl>
<h2>Arbitrary Executable Modules</h2>
<p> The current approach is to create a wrapper python plugin, which holds the meta data and calls the binaries as necessary (see the examples). </p>
<h2>Examples</h2>
<dl>
<dt>Flow description (Example 1):</p>
<dd> Consider the following flow and its dictionary:<br />
&nbsp;<wbr>start-&gt;fix-&gt;end<br />
&nbsp;<wbr>dict&nbsp;<wbr>=&nbsp;<wbr>{&nbsp;<wbr>start:fix,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fix:end<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>} </p>
<dt>Flow description (Example 2):</p>
<dd> Consider the following flow and its dictionary:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>,&gt;end<br />
&nbsp;<wbr>start-&gt;diagnose<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>`&gt;fix-&gt;end<br />
&nbsp;<wbr>dict&nbsp;<wbr>=&nbsp;<wbr>{&nbsp;<wbr>start:diagnose,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>diagnose:{&quot;goodSys&quot;:end,&quot;badSys&quot;:fix},&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fix:end&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>} </p>
<p> This flow has a conditional after the diagnose function. If diagnose results in a corrupt state of the system, then the plugin proceeds with fix. If all is good in the system, then the flow end. Note that the next step in the diagnose case is defined buy whatever diagnose returned. </p>
<dt>Adding a flow (Example 3):</p>
<dd> class MyPlugin(Plugin):<br />
&nbsp;<wbr>flows&nbsp;<wbr>=&nbsp;<wbr>Flow.init(Plugin)<br />
&nbsp;<wbr>flows[&quot;myflow&quot;]&nbsp;<wbr>=&nbsp;<wbr>Flow({flow rules}, description=&quot;&quot;) </p>
</dl>
<h2>SEE ALSO</h2>
<p> firstaidkit-reporting manpage firstaidkit-backup manpage <a rel="nofollow" href="http://fedorahosted.org/firstaidkit">http://fedorahosted.org/firstaidkit</a> </p>
<h2>AUTHORS</h2>
<p> Martin Sivak &lt;msivak [at] redhat.com&gt; Joel Granados &lt;jgranado [at] redhat.com&gt; </p>
<h2>BUGS</h2>
<p> Please search/report bugs at <a rel="nofollow" href="http://fedorahosted.org/firstaidkit/newticket">http://fedorahosted.org/firstaidkit/newticket</a> </p>
<h2>Index</h2>
