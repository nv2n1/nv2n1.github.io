---
title: "tcl_setensembleparameterlist(3)"
name: "tcl_setensembleparameterlist"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_setensembleparameterlist/"
description: "Tcl_CreateEnsemble, Tcl_FindEnsemble, Tcl_GetEnsembleFlags, Tcl_GetEnsembleMappingDict, Tcl_GetEnsembleNamespace, Tcl_GetEnsembleParameterList, Tcl_GetEnsembleUnknownHandler, Tcl_GetEnsembleSubcomm..."
---

<p>Tcl_CreateEnsemble, Tcl_FindEnsemble, Tcl_GetEnsembleFlags, Tcl_GetEnsembleMappingDict, Tcl_GetEnsembleNamespace, Tcl_GetEnsembleParameterList, Tcl_GetEnsembleUnknownHandler, Tcl_GetEnsembleSubcommandList, Tcl_IsEnsemble, Tcl_SetEnsembleFlags, Tcl_SetEnsembleMappingDict, Tcl_SetEnsembleParameterList, Tcl_SetEnsembleSubcommandList, Tcl_SetEnsembleUnknownHandler &#8211; manipulate ensemble commands </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Command
<code>Tcl_CreateEnsemble</code>(<i>interp, name, namespacePtr, ensFlags</i>)
Tcl_Command
<code>Tcl_FindEnsemble</code>(<i>interp, cmdNameObj, flags</i>)
int
<code>Tcl_IsEnsemble</code>(<i>token</i>)
int
<code>Tcl_GetEnsembleFlags</code>(<i>interp, token, ensFlagsPtr</i>)
int
<code>Tcl_SetEnsembleFlags</code>(<i>interp, token, ensFlags</i>)
int
<code>Tcl_GetEnsembleMappingDict</code>(<i>interp, token, dictObjPtr</i>)
int
<code>Tcl_SetEnsembleMappingDict</code>(<i>interp, token, dictObj</i>)
int
<code>Tcl_GetEnsembleParameterList</code>(<i>interp, token, listObjPtr</i>)
int
<code>Tcl_SetEnsembleParameterList</code>(<i>interp, token, listObj</i>)
int
<code>Tcl_GetEnsembleSubcommandList</code>(<i>interp, token, listObjPtr</i>)
int
<code>Tcl_SetEnsembleSubcommandList</code>(<i>interp, token, listObj</i>)
int
<code>Tcl_GetEnsembleUnknownHandler</code>(<i>interp, token, listObjPtr</i>)
int
<code>Tcl_SetEnsembleUnknownHandler</code>(<i>interp, token, listObj</i>)
int
<code>Tcl_GetEnsembleNamespace</code>(<i>interp, token, namespacePtrPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in/out) The interpreter in which the ensemble is to be created or found. Also where error result messages are written. The functions whose names start with <code>Tcl_GetEnsemble</code> may have a NULL for the <i>interp</i>, but all other functions must not.</p>
<dd>const char <i>*name</i> (in) The name of the ensemble command to be created.</p>
<dd>Tcl_Namespace <i>*namespacePtr</i> (in) The namespace to which the ensemble command is to be bound, or NULL for the current namespace.</p>
<dd>int <i>ensFlags</i> (in) An ORed set of flag bits describing the basic configuration of the ensemble. Currently only one bit has meaning, <code>TCL_ENSEMBLE_PREFIX</code>, which is present when the ensemble command should also match unambiguous prefixes of subcommands.</p>
<dd>Tcl_Obj <i>*cmdNameObj</i> (in) A value holding the name of the ensemble command to look up.</p>
<dd>int <i>flags</i> (in) An ORed set of flag bits controlling the behavior of <code>Tcl_FindEnsemble</code>. Currently only <code>TCL_LEAVE_ERR_MSG</code> is supported.</p>
<dd>Tcl_Command <i>token</i> (in) A normal command token that refers to an ensemble command, or which you wish to use for testing as an ensemble command in <code>Tcl_IsEnsemble</code>.</p>
<dd>int <i>*ensFlagsPtr</i> (out) Pointer to a variable into which to write the current ensemble flag bits; currently only the bit <code>TCL_ENSEMBLE_PREFIX</code> is defined.</p>
<dd>Tcl_Obj <i>*dictObj</i> (in) A dictionary value to use for the subcommand to implementation command prefix mapping dictionary in the ensemble. May be NULL if the mapping dictionary is to be removed.</p>
<dd>Tcl_Obj <i>**dictObjPtr</i> (out) Pointer to a variable into which to write the current ensemble mapping dictionary.</p>
<dd>Tcl_Obj <i>*listObj</i> (in) A list value to use for the list of formal pre-subcommand parameters, the defined list of subcommands in the dictionary or the unknown subcommand handler command prefix. May be NULL if the subcommand list or unknown handler are to be removed.</p>
<dd>Tcl_Obj <i>**listObjPtr</i> (out) Pointer to a variable into which to write the current list of formal pre-subcommand parameters, the defined list of subcommands or the current unknown handler prefix.</p>
<dd>Tcl_Namespace <i>**namespacePtrPtr</i> (out) Pointer to a variable into which to write the handle of the namespace to which the ensemble is bound.
</dl>
<h2>Description</h2>
<p>An ensemble is a command, bound to some namespace, which consists of a collection of subcommands implemented by other Tcl commands. The first argument to the ensemble command is always interpreted as a selector that states what subcommand to execute. </p>
<p> Ensembles are created using <code>Tcl_CreateEnsemble</code>, which takes four arguments: the interpreter to work within, the name of the ensemble to create, the namespace within the interpreter to bind the ensemble to, and the default set of ensemble flags. The result of the function is the command token for the ensemble, which may be used to further configure the ensemble using the API described below in <code>ENSEMBLE PROPERTIES</code>. </p>
<p> Given the name of an ensemble command, the token for that command may be retrieved using <code>Tcl_FindEnsemble</code>. If the given command name (in <i>cmdNameObj</i>) does not refer to an ensemble command, the result of the function is NULL and (if the <code>TCL_LEAVE_ERR_MSG</code> bit is set in <i>flags</i>) an error message is left in the interpreter result. </p>
<p> A command token may be checked to see if it refers to an ensemble using <code>Tcl_IsEnsemble</code>. This returns 1 if the token refers to an ensemble, or 0 otherwise.</p>
<h3>Ensemble Properties</h3>
<p>Every ensemble has four read-write properties and a read-only property. The properties are:</p>
<dl COMPACT>
<dt><code>flags</code> (read-write)</p>
<dd>The set of flags for the ensemble, expressed as a bit-field. Currently, the only public flag is <code>TCL_ENSEMBLE_PREFIX</code> which is set when unambiguous prefixes of subcommands are permitted to be resolved to implementations as well as exact matches. The flags may be read and written using <code>Tcl_GetEnsembleFlags</code> and <code>Tcl_SetEnsembleFlags</code> respectively. The result of both of those functions is a Tcl result code (<code>TCL_OK</code>, or <code>TCL_ERROR</code> if the token does not refer to an ensemble).</p>
<dt><code>mapping dictionary</code> (read-write)</p>
<dd>A dictionary containing a mapping from subcommand names to lists of words to use as a command prefix (replacing the first two words of the command which are the ensemble command itself and the subcommand name), or NULL if every subcommand is to be mapped to the command with the same unqualified name in the ensemble&#8217;s bound namespace. Defaults to NULL. May be read and written using <code>Tcl_GetEnsembleMappingDict</code> and <code>Tcl_SetEnsembleMappingDict</code> respectively. The result of both of those functions is a Tcl result code (<code>TCL_OK</code>, or <code>TCL_ERROR</code> if the token does not refer to an ensemble) and the dictionary obtained from <code>Tcl_GetEnsembleMappingDict</code> should always be treated as immutable even if it is unshared. All command names in prefixes set via <code>Tcl_SetEnsembleMappingDict</code> must be fully qualified.</p>
<dt><code>formal pre-subcommand parameter list</code> (read-write)</p>
<dd>A list of formal parameter names (the names only being used when generating error messages) that come at invocation of the ensemble between the name of the ensemble and the subcommand argument. NULL (the default) is equivalent to the empty list. May be read and written using <code>Tcl_GetEnsembleParameterList</code> and <code>Tcl_SetEnsembleParameterList</code> respectively. The result of both of those functions is a Tcl result code (<code>TCL_OK</code>, or <code>TCL_ERROR</code> if the token does not refer to an ensemble) and the dictionary obtained from <code>Tcl_GetEnsembleParameterList</code> should always be treated as immutable even if it is unshared.</p>
<dt><code>subcommand list</code> (read-write)</p>
<dd>A list of all the subcommand names for the ensemble, or NULL if this is to be derived from either the keys of the mapping dictionary (see above) or (if that is also NULL) from the set of commands exported by the bound namespace. May be read and written using <code>Tcl_GetEnsembleSubcommandList</code> and <code>Tcl_SetEnsembleSubcommandList</code> respectively. The result of both of those functions is a Tcl result code (<code>TCL_OK</code>, or <code>TCL_ERROR</code> if the token does not refer to an ensemble) and the list obtained from <code>Tcl_GetEnsembleSubcommandList</code> should always be treated as immutable even if it is unshared.</p>
<dt><code>unknown subcommand handler command prefix</code> (read-write)</p>
<dd>A list of words to prepend on the front of any subcommand when the subcommand is unknown to the ensemble (according to the current prefix handling rule); see the <code>namespace ensemble</code> command for more details. If NULL, the default behavior &#8211; generate a suitable error message &#8211; will be used when an unknown subcommand is encountered. May be read and written using <code>Tcl_GetEnsembleUnknownHandler</code> and <code>Tcl_SetEnsembleUnknownHandler</code> respectively. The result of both functions is a Tcl result code (<code>TCL_OK</code>, or <code>TCL_ERROR</code> if the token does not refer to an ensemble) and the list obtained from <code>Tcl_GetEnsembleUnknownHandler</code> should always be treated as immutable even if it is unshared.</p>
<dt><code>bound namespace</code> (read-only)</p>
<dd>The namespace to which the ensemble is bound; when the namespace is deleted, so too will the ensemble, and this namespace is also the namespace whose list of exported commands is used if both the mapping dictionary and the subcommand list properties are NULL. May be read using <code>Tcl_GetEnsembleNamespace</code> which returns a Tcl result code (<code>TCL_OK</code>, or <code>TCL_ERROR</code> if the token does not refer to an ensemble).</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/n-namespace/">namespace</a>(n), <a href="/docs/linux/man/3-tcl_deletecommandfromtoken/">Tcl_DeleteCommandFromToken</a>(3)</p>
<h2>Keywords</h2>
<p>command, ensemble</p>
