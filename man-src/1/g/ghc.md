---

title: "ghc(1)"
name: "ghc"
section: "1"
letter: "g"
url: "/docs/linux/man/1-ghc/"
description: "GHC – the Glasgow Haskell Compiler"
---

<p> GHC &#8211; the Glasgow Haskell Compiler </p>
<h2>SYNOPSIS</h2>
<p> <code>ghc</code> [<i>option</i>|<i>filename</i>]&#8230;<br />
 <code>ghci</code> [<i>option</i>|<i>filename</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>ghc</code> and <code>ghci</code> commands. Note that <code>ghci</code> is not yet available on all architectures. Extensive documentation is available in various other formats including DVI, PostScript and HTML; see below. </p>
<p> Each of GHC&#8217;s command line options is classified as either <i>static</i> or <i>dynamic</i>. A static flag may only be specified on the command line, whereas a dynamic flag may also be given in an OPTIONS pragma in a source file or set from the GHCi command-line with :set. </p>
<p> As a rule of thumb, all the language options are dynamic, as are the warning options and the debugging options. </p>
<p> The rest are static, with the notable exceptions of <code>-v</code>, <code>-cpp</code>, <code>-fasm</code>, <code>-fvia-C</code>, <code>-fllvm</code>, and &quot; -#include . The OPTIONS sections lists the status of each flag. </p>
<p> Common suffixes of file names for Haskell are:</p>
<dl>
<dt><code>.hs</code></dt>
<dd> Haskell source code; preprocess, compile</dd>
<dt><code>.lhs</code></dt>
<dd> literate Haskell source; unlit, preprocess, compile</dd>
<dt><code>.hi</code></dt>
<dd> Interface file; contains information about exported symbols</dd>
<dt><code>.hc</code></dt>
<dd> intermediate C files</dd>
<dt><code>.</code><i>x</i><code>_o</code></dt>
<dd> way <i>x</i> object files; common ways are: <code>p</code>, <code>u</code>, <code>s</code></dd>
<dt><code>.</code><i>x</i><code>_hi</code></dt>
<dd> way <i>x</i> interface files </dd>
</dl>
<h2>OPTIONS</h2>
<h3>Help and verbosity options</h3>
<p> -? -help -v -v<i>n</i> -V &#8211;supported-extensions or &#8211;supported-languages &#8211;info &#8211;version &#8211;numeric-version &#8211;print-libdir -ferror-spans -H<i>size</i> -Rghc-timing </p>
<h3>Which phases to run</h3>
<p> -E -C -S -c -x <i>suffix</i> </p>
<h3>Alternative modes of operation</h3>
<p> &#8211;interactive &#8211;make -e expr -M </p>
<h3>Redirecting output</h3>
<p> -hcsuf <i>suffix</i> -hidir <i>dir</i> -hisuf <i>suffix</i> -o <i>filename</i> -odir <i>dir</i> -ohi <i>filename</i> -osuf <i>suffix</i> -stubdir <i>dir</i> -dumpdir <i>dir</i> -outputdir <i>dir</i> </p>
<h3>Keeping intermediate files</h3>
<p> -keep-hc-file or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-keep-hc-files&nbsp;<wbr>&nbsp;<wbr>-keep-llvm-file or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-keep-llvm-files&nbsp;<wbr>&nbsp;<wbr>-keep-s-file or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-keep-s-files&nbsp;<wbr>&nbsp;<wbr>-keep-tmp-files&nbsp;<wbr>&nbsp;<wbr> </p>
<h3>Temporary files</h3>
<p> -tmpdir </p>
<h3>Finding imports</h3>
<p> -i<i>dir1</i>:<i>dir2</i>:&#8230; -i </p>
<h3>Interface file options</h3>
<p> -ddump-hi -ddump-hi-diffs -ddump-minimal-imports &#8211;show-iface <i>file</i> </p>
<h3>Recompilation checking</h3>
<p> -fforce-recomp -fno-force-recomp </p>
<h3>Interactive-mode options</h3>
<p> -ignore-dot-ghci -ghci-script -fbreak-on-exception -fno-break-on-exception -fbreak-on-error -fno-break-on-error -fprint-evld-with-show -fno-print-evld-with-show -fprint-bind-result -fno-print-bind-result -fno-print-bind-contents -fno-implicit-import-qualified -interactive-print </p>
<h3>Packages</h3>
<p> -package-name <i>P</i> -package <i>P</i> -hide-all-packages -hide-package <i>name</i> -ignore-package <i>name</i> -package-db <i>file</i> -clear-package-db -no-global-package-db -global-package-db -no-user-package-db -user-package-db -no-auto-link-packages -trust <i>P</i> -distrust <i>P</i> -distrust-all </p>
<h3>Language options</h3>
<p> -fglasgow-exts -fno-glasgow-exts -XOverlappingInstances -XNoOverlappingInstances -XIncoherentInstances -XNoIncoherentInstances -XUndecidableInstances -XNoUndecidableInstances -fcontext-stack=N<i>n</i> -XArrows -XNoArrows -XDisambiguateRecordFields -XNoDisambiguateRecordFields -XForeignFunctionInterface -XNoForeignFunctionInterface -XGenerics -XNoGenerics -XImplicitParams -XNoImplicitParams -firrefutable-tuples -fno-irrefutable-tuples -XNoImplicitPrelude -XImplicitPrelude -XRebindableSyntax -XNoRebindableSyntax -XNoMonomorphismRestriction -XMonomorphismRrestriction -XNoNPlusKPatterns -XNPlusKPatterns -XNoTraditionalRecordSyntax -XTraditionalRecordSyntax -XNoMonoPatBinds -XMonoPatBinds -XRelaxedPolyRec -XNoRelaxedPolyRec -XExtendedDefaultRules -XNoExtendedDefaultRules -XOverloadedStrings -XNoOverloadedStrings -XGADTs -XNoGADTs -XGADTSyntax -XNoGADTSyntax -XTypeFamilies -XNoTypeFamilies -XConstraintKinds -XNoConstraintKinds -XDataKinds -XNoDataKinds -XPolyKinds -XNoPolyKinds -XScopedTypeVariables -XNoScopedTypeVariables -XMonoLocalBinds -XNoMonoLocalBinds -XTemplateHaskell -XNoTemplateHaskell -XQuasiQuotes -XNoQuasiQuotes -XBangPatterns -XNoBangPatterns -XCPP -XNoCPP -XPatternGuards -XNoPatternGuards -XViewPatterns -XNoViewPatterns -XUnicodeSyntax -XNoUnicodeSyntax -XMagicHash -XNoMagicHash -XExplicitForAll -XNoExplicitForAll -XPolymorphicComponents -XNoPolymorphicComponents -XRank2Types -XNoRank2Types -XRankNTypes -XNoRankNTypes -XImpredicativeTypes -XNoImpredicativeTypes -XExistentialQuantification -XNoExistentialQuantification -XKindSignatures -XNoKindSignatures -XEmptyDataDecls -XNoEmptyDataDecls -XParallelListComp -XNoParallelListComp -XTransformListComp -XNoTransformListComp -XMonadComprehensions -XNoMonadComprehensions -XUnliftedFFITypes -XNoUnliftedFFITypes -XInterruptibleFFI -XNoInterruptibleFFI -XLiberalTypeSynonyms -XNoLiberalTypeSynonyms -XTypeOperators -XNoTypeOperators -XExplicitNamespaces -XNoExplicitNamespaces -XRecursiveDo -XNoRecursiveDo -XParallelArrays -XNoParallelArrays -XRecordWildCards -XNoRecordWildCards -XNamedFieldPuns -XNoNamedFieldPuns -XDisambiguateRecordFields -XNoDisambiguateRecordFields -XUnboxedTuples -XNoUnboxedTuples -XStandaloneDeriving -XNoStandaloneDeriving -XDeriveDataTypeable -XNoDeriveDataTypeable -XDeriveGeneric -XNoDeriveGeneric -XGeneralizedNewtypeDeriving -XNoGeneralizedNewtypeDeriving -XTypeSynonymInstances -XNoTypeSynonymInstances -XFlexibleContexts -XNoFlexibleContexts -XFlexibleInstances -XNoFlexibleInstances -XConstrainedClassMethods -XNoConstrainedClassMethods -XDefaultSignatures -XNoDefaultSignatures -XMultiParamTypeClasses -XNoMultiParamTypeClasses -XFunctionalDependencies -XNoFunctionalDependencies -XPackageImports -XNoPackageImports -XLambdaCase -XNoLambdaCase -XMultiWayIf -XNoMultiWayIf -XSafe -XTrustworthy -XUnsafe -fpackage-trust </p>
<h3>Warnings</h3>
<p> -W -w -w -Wall -w -Werror -Wwarn -fdefer-type-errors -fno-defer-type-errors -fhelpful-errors -fno-helpful-errors -fwarn-deprecated-flags -fno-warn-deprecated-flags -fwarn-duplicate-exports -fno-warn-duplicate-exports -fwarn-hi-shadowing -fno-warn-hi-shadowing -fwarn-identities -fno-warn-identities -fwarn-implicit-prelude -fno-warn-implicit-prelude -fwarn-incomplete-patterns -fno-warn-incomplete-patterns -fwarn-incomplete-uni-patterns -fno-warn-incomplete-uni-patterns -fwarn-incomplete-record-updates -fno-warn-incomplete-record-updates -fwarn-lazy-unlifted-bindings -fno-warn-lazy-unlifted-bindings -fwarn-missing-fields -fno-warn-missing-fields -fwarn-missing-import-lists -fnowarn-missing-import-lists -fwarn-missing-methods -fno-warn-missing-methods -fwarn-missing-signatures -fno-warn-missing-signatures -fwarn-missing-local-sigs -fno-warn-missing-local-sigs -fwarn-monomorphism-restriction -fno-warn-monomorphism-restriction -fwarn-name-shadowing -fno-warn-name-shadowing -fwarn-orphans, -fwarn-auto-orphans -fno-warn-orphans, -fno-warn-auto-orphans -fwarn-overlapping-patterns -fno-warn-overlapping-patterns -fwarn-tabs -fno-warn-tabs -fwarn-type-defaults -fno-warn-type-defaults -fwarn-unrecognised-pragmas -fno-warn-unrecognised-pragmas -fwarn-unused-binds -fno-warn-unused-binds -fwarn-unused-imports -fno-warn-unused-imports -fwarn-unused-matches -fno-warn-unused-matches -fwarn-unused-do-bind -fno-warn-unused-do-bind -fwarn-wrong-do-bind -fno-warn-wrong-do-bind -fwarn-unsafe -fno-warn-unsafe -fwarn-safe -fno-warn-safe -fwarn-warnings-deprecations -fno-warn-warnings-deprecations </p>
<h3>Optimisation levels</h3>
<p> -O -O0 -O<i>n</i> -O0 </p>
<h3>Individual optimisations</h3>
<p> -fcase-merge -fno-case-merge -fcse -fdicts-strict -fno-dicts-strict -fdo-eta-reduction -fno-do-eta-reduction -fdo-lambda-eta-expansion -fno-do-lambda-eta-expansion -feager-blackholing -fenable-rewrite-rules -fno-enable-rewrite-rules -fvectorise -fno-vectorise -favoid-vect -fno-avoid-vect -fexcess-precision -fno-excess-precision -ffloat-in -ffull-laziness -fignore-asserts -fno-ignore-asserts -fignore-interface-pragmas -fno-ignore-interface-pragmas -fliberate-case -fliberate-case-threshold=<i>n</i> -fno-liberate-case-threshold -fmax-simplifier-iterations -fmax-worker-args -fno-opt-coercion -fno-pre-inlining -fno-state-hack -fpedantic-bottoms -fno-pedantic-bottoms -fomit-interface-pragmas -fno-omit-interface-pragmas -fsimplifier-phases -fsimpl-tick-factor=n -fspec-constr -fspec-constr-threshold=<i>n</i> -fno-spec-constr-threshold -fspec-constr-count=<i>n</i> -fno-spec-constr-count -fspecialise -fstrictness -fstrictness=before=<i>n</i> -fstatic-argument-transformation -funbox-strict-fields -fno-unbox-strict-fields -funfolding-creation-threshold -fno-unfolding-creation-threshold -funfolding-fun-discount -fno-unfolding-fun-discount -funfolding-keeness-factor -fno-unfolding-keeness-factor -funfolding-use-threshold -fno-unfolding-use-threshold </p>
<h3>Profiling options</h3>
<p> -prof -fprof-auto -fno-prof-auto -fprof-auto-top -fno-prof-auto -fprof-auto-exported -fno-prof-auto -fprof-cafs -fno-prof-cafs -fno-prof-count-entries -fprof-count-entries -ticky </p>
<h3>Program coverage options</h3>
<p> -fhpc -hpcdir dir </p>
<h3>Haskell pre-processor options</h3>
<p> -F </p>
<h3>C pre-processor options</h3>
<p> -cpp -D<i>symbol</i>=<i>value</i> -U -U<i>symbol</i> -I<i>dir</i> </p>
<h3>Code generation options</h3>
<p> -fasm -fllvm -fno-code -fbyte-code -fobject-code </p>
<h3>Linking options</h3>
<p> -shared -fPIC -dynamic -dynload -framework <i>name</i> -framework-path <i>name</i> -l<i>lib</i> -L<i>dir</i> -main-is &#8211;mk-dll -no-hs-main -rtsopts, -rtsopts={none,some,all} -with-rtsopts=opts -no-link -split-objs -static -threaded -debug -eventlog -fno-gen-manifest -fno-embed-manifest -fno-shared-implib -dylib-install-name <i>path</i> </p>
<h3>Plugin options</h3>
<p> -fplugin=<i>module</i> -fplugin-opt=<i>module:args</i> </p>
<h3>Replacing phases</h3>
<p> -pgmL <i>cmd</i> -pgmP <i>cmd</i> -pgmc <i>cmd</i> -pgms <i>cmd</i> -pgma <i>cmd</i> -pgml <i>cmd</i> -pgmdll <i>cmd</i> -pgmF <i>cmd</i> -pgmwindres <i>cmd</i> </p>
<h3>Forcing options to particular phases</h3>
<p> -optL <i>option</i> -optP <i>option</i> -optF <i>option</i> -optc <i>option</i> -optlo <i>option</i> -optlc <i>option</i> -optm <i>option</i> -opta <i>option</i> -optl <i>option</i> -optdll <i>option</i> -optwindres <i>option</i> </p>
<h3>Platform-specific options</h3>
<p> -msse2 -monly-[432]-regs </p>
<h3>External core file options</h3>
<p> -fext-core </p>
<h3>Compiler debugging options</h3>
<p> -dcore-lint -ddump-to-file -ddump-asm -ddump-bcos -ddump-cmm -ddump-core-stats -ddump-cpranal -ddump-cse -ddump-deriv -ddump-ds -ddump-flatC -ddump-foreign -ddump-hpc -ddump-inlinings -ddump-llvm -ddump-occur-anal -ddump-opt-cmm -ddump-parsed -ddump-prep -ddump-rn -ddump-rule-firings -ddump-rule-rewrites -ddump-rules -ddump-vect -ddump-simpl -ddump-simpl-phases -ddump-simpl-iterations -ddump-spec -ddump-splices -ddump-stg -ddump-stranal -ddump-tc -ddump-types -ddump-worker-wrapper -ddump-if-trace -ddump-tc-trace -ddump-vt-trace -ddump-rn-trace -ddump-rn-stats -ddump-simpl-stats -dno-debug-output -dppr-debug -dppr-noprags -dppr-user-length -dppr-colsNNN -dppr-case-as-let -dsuppress-all -dsuppress-uniques -dsuppress-idinfo -dsuppress-module-prefixes -dsuppress-type-signatures -dsuppress-type-applications -dsuppress-coercions -dsource-stats -dcmm-lint -dstg-lint -dstg-stats -dverbose-core2core -dverbose-stg2stg -dshow-passes -dfaststring-stats </p>
<h3>Misc compiler options</h3>
<p> -fno-hi-version-check -dno-black-holing -fhistory-size -funregisterised -fno-ghci-history -fno-ghci-sandbox </p>
<h2>HELP AND VERBOSITY OPTIONS</h2>
<dl>
<dt><code>-?</code></dt>
<dd> help [mode] </dd>
<dt><code>-help</code></dt>
<dd> help [mode] </dd>
<dt><code>-v</code></dt>
<dd> verbose mode (equivalent to <code>-v3</code>) [dynamic] </dd>
<dt><code>-v</code><i>n</i></dt>
<dd> set verbosity level [dynamic] </dd>
<dt><code>-V</code></dt>
<dd> display GHC version [mode] </dd>
<dt><code>&#8211;supported-extensions</code> or <code>&#8211;supported-languages</code></dt>
<dd> display the supported languages and language extensions [mode] </dd>
<dt><code>&#8211;info</code></dt>
<dd> display information about the compiler [mode] </dd>
<dt><code>&#8211;version</code></dt>
<dd> display GHC version [mode] </dd>
<dt><code>&#8211;numeric-version</code></dt>
<dd> display GHC version (numeric only) [mode] </dd>
<dt><code>&#8211;print-libdir</code></dt>
<dd> display GHC library directory [mode] </dd>
<dt><code>-ferror-spans</code></dt>
<dd> output full span in error messages [static] </dd>
<dt><code>-H</code><i>size</i></dt>
<dd> Set the minimum heap size to <i>size</i> [static] </dd>
<dt><code>-Rghc-timing</code></dt>
<dd> Summarise timing stats for GHC (same as +RTS -tstderr) [static] </dd>
</dl>
<h2>WHICH PHASES TO RUN</h2>
<dl>
<dt><code>-E</code></dt>
<dd> Stop after preprocessing (.hspp file) [mode] </dd>
<dt><code>-C</code></dt>
<dd> Stop after generating C (.hc file) [mode] </dd>
<dt><code>-S</code></dt>
<dd> Stop after generating assembly (.s file) [mode] </dd>
<dt><code>-c</code></dt>
<dd> Do not link [dynamic] </dd>
<dt><code>-x</code> <i>suffix</i></dt>
<dd> Override default behaviour for source files [static] </dd>
</dl>
<h2>ALTERNATIVE MODES OF OPERATION</h2>
<dl>
<dt><code>&#8211;interactive</code></dt>
<dd> Interactive mode &#8211; normally used by just running ghci; see for details. [mode] </dd>
<dt><code>&#8211;make</code></dt>
<dd> Build a multi-module Haskell program, automatically figuring out dependencies. Likely to be much easier, and faster, than using make; see for details.. [mode] </dd>
<dt><code>-e expr</code></dt>
<dd> Evaluate <i>expr</i>; see for details. [mode] </dd>
<dt><code>-M</code></dt>
<dd> Generate dependency information suitable for use in a Makefile; see for details. [mode] </dd>
</dl>
<h2>REDIRECTING OUTPUT</h2>
<dl>
<dt><code>-hcsuf</code> <i>suffix</i></dt>
<dd> set the suffix to use for intermediate C files [dynamic] </dd>
<dt><code>-hidir</code> <i>dir</i></dt>
<dd> set directory for interface files [dynamic] </dd>
<dt><code>-hisuf</code> <i>suffix</i></dt>
<dd> set the suffix to use for interface files [dynamic] </dd>
<dt><code>-o</code> <i>filename</i></dt>
<dd> set output filename [dynamic] </dd>
<dt><code>-odir</code> <i>dir</i></dt>
<dd> set directory for object files [dynamic] </dd>
<dt><code>-ohi</code> <i>filename</i></dt>
<dd> set the filename in which to put the interface [dynamic] </dd>
<dt><code>-osuf</code> <i>suffix</i></dt>
<dd> set the output file suffix [dynamic] </dd>
<dt><code>-stubdir</code> <i>dir</i></dt>
<dd> redirect FFI stub files [dynamic] </dd>
<dt><code>-dumpdir</code> <i>dir</i></dt>
<dd> redirect dump files [dynamic] </dd>
<dt><code>-outputdir</code> <i>dir</i></dt>
<dd> set output directory [dynamic] </dd>
</dl>
<h2>KEEPING INTERMEDIATE FILES</h2>
<dl>
<dt><code>-keep-hc-file</code> or</dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-keep-hc-files</code>&nbsp;<wbr> retain intermediate .hc files [dynamic] </dd>
<dt><code>-keep-llvm-file</code> or</dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-keep-llvm-files</code>&nbsp;<wbr> retain intermediate LLVM .ll files [dynamic] </dd>
<dt><code>-keep-s-file</code> or</dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>-keep-s-files</code>&nbsp;<wbr> retain intermediate .s files [dynamic] </dd>
<dt><code>-keep-tmp-files</code></dt>
<dd> retain all intermediate temporary files [dynamic] </dd>
</dl>
<h2>TEMPORARY FILES</h2>
<dl>
<dt><code>-tmpdir</code></dt>
<dd> set the directory for temporary files [dynamic] </dd>
</dl>
<h2>FINDING IMPORTS</h2>
<dl>
<dt><code>-i</code><i>dir1</i>:<i>dir2</i>:&#8230;</dt>
<dd> add <i>dir</i>, <i>dir2</i>, etc. to import path [static/:set] </dd>
<dt><code>-i</code></dt>
<dd> Empty the import directory list [static/:set] </dd>
</dl>
<h2>INTERFACE FILE OPTIONS</h2>
<dl>
<dt><code>-ddump-hi</code></dt>
<dd> Dump the new interface to stdout [dynamic] </dd>
<dt><code>-ddump-hi-diffs</code></dt>
<dd> Show the differences vs. the old interface [dynamic] </dd>
<dt><code>-ddump-minimal-imports</code></dt>
<dd> Dump a minimal set of imports [dynamic] </dd>
<dt><code>&#8211;show-iface</code> <i>file</i></dt>
<dd> See . [] </dd>
</dl>
<h2>RECOMPILATION CHECKING</h2>
<dl>
<dt><code>-fforce-recomp</code></dt>
<dd> Turn off recompilation checking; implied by any <code>-ddump-X</code> option [dynamic] </dd>
</dl>
<h2>INTERACTIVE-MODE OPTIONS</h2>
<dl>
<dt><code>-ignore-dot-ghci</code></dt>
<dd> Disable reading of .ghci files [dynamic] </dd>
<dt><code>-ghci-script</code></dt>
<dd> Read additional .ghci files [dynamic] </dd>
<dt><code>-fbreak-on-exception</code></dt>
<dd> Break on any exception thrown [dynamic] </dd>
<dt><code>-fbreak-on-error</code></dt>
<dd> Break on uncaught exceptions and errors [dynamic] </dd>
<dt><code>-fprint-evld-with-show</code></dt>
<dd> Enable usage of Show instances in :print [dynamic] </dd>
<dt><code>-fprint-bind-result</code></dt>
<dd> Turn on printing of binding results in GHCi [dynamic] </dd>
<dt><code>-fno-print-bind-contents</code></dt>
<dd> Turn off printing of binding contents in GHCi [dynamic] </dd>
<dt><code>-fno-implicit-import-qualified</code></dt>
<dd> Turn off implicit qualified import of everything in GHCi [dynamic] </dd>
<dt><code>-interactive-print</code></dt>
<dd> Select the function to use for printing evaluated expressions in GHCi [dynamic] </dd>
</dl>
<h2>PACKAGES</h2>
<dl>
<dt><code>-package-name</code> <i>P</i></dt>
<dd> Compile to be part of package <i>P</i> [static] </dd>
<dt><code>-package</code> <i>P</i></dt>
<dd> Expose package <i>P</i> [static/:set] </dd>
<dt><code>-hide-all-packages</code></dt>
<dd> Hide all packages by default [static] </dd>
<dt><code>-hide-package</code> <i>name</i></dt>
<dd> Hide package <i>P</i> [static/:set] </dd>
<dt><code>-ignore-package</code> <i>name</i></dt>
<dd> Ignore package <i>P</i> [static/:set] </dd>
<dt><code>-package-db</code> <i>file</i></dt>
<dd> Add <i>file</i> to the package db stack. [static] </dd>
<dt><code>-clear-package-db</code></dt>
<dd> Clear the package db stack. [static] </dd>
<dt><code>-no-global-package-db</code></dt>
<dd> Remove the global package db from the stack. [static] </dd>
<dt><code>-global-package-db</code></dt>
<dd> Add the global package db to the stack. [static] </dd>
<dt><code>-no-user-package-db</code></dt>
<dd> Remove the user&#8217;s package db from the stack. [static] </dd>
<dt><code>-user-package-db</code></dt>
<dd> Add the user&#8217;s package db to the stack. [static] </dd>
<dt><code>-no-auto-link-packages</code></dt>
<dd> Don&#8217;t automatically link in the haskell98 package. [dynamic] </dd>
<dt><code>-trust</code> <i>P</i></dt>
<dd> Expose package <i>P</i> and set it to be trusted [static/:set] </dd>
<dt><code>-distrust</code> <i>P</i></dt>
<dd> Expose package <i>P</i> and set it to be distrusted [static/:set] </dd>
<dt><code>-distrust-all</code></dt>
<dd> Distrust all packages by default [static/:set] </dd>
</dl>
<h2>LANGUAGE OPTIONS</h2>
<dl>
<dt><code>-fglasgow-exts</code></dt>
<dd> Enable most language extensions; see for exactly which ones. [dynamic] </dd>
<dt><code>-XOverlappingInstances</code></dt>
<dd> Enable overlapping instances [dynamic] </dd>
<dt><code>-XIncoherentInstances</code></dt>
<dd> Enable incoherent instances. Implies <code>-XOverlappingInstances</code> [dynamic] </dd>
<dt><code>-XUndecidableInstances</code></dt>
<dd> Enable undecidable instances [dynamic] </dd>
<dt><code>-fcontext-stack=N</code><i>n</i></dt>
<dd> set the limit for context reduction. Default is 20. [dynamic] </dd>
<dt><code>-XArrows</code></dt>
<dd> Enable arrow notation extension [dynamic] </dd>
<dt><code>-XDisambiguateRecordFields</code></dt>
<dd> Enable record field disambiguation [dynamic] </dd>
<dt><code>-XForeignFunctionInterface</code></dt>
<dd> Enable foreign function interface (implied by <code>-fglasgow-exts</code>) [dynamic] </dd>
<dt><code>-XGenerics</code></dt>
<dd> Deprecated, does nothing. No longer enables generic classes. See also GHC&#8217;s support for generic programming. [dynamic] </dd>
<dt><code>-XImplicitParams</code></dt>
<dd> Enable Implicit Parameters. Implied by <code>-fglasgow-exts</code>. [dynamic] </dd>
<dt><code>-firrefutable-tuples</code></dt>
<dd> Make tuple pattern matching irrefutable [dynamic] </dd>
<dt><code>-XNoImplicitPrelude</code></dt>
<dd> Don&#8217;t implicitly import Prelude [dynamic] </dd>
<dt><code>-XRebindableSyntax</code></dt>
<dd> Employ rebindable syntax [dynamic] </dd>
<dt><code>-XNoMonomorphismRestriction</code></dt>
<dd> Disable the monomorphism restriction [dynamic] </dd>
<dt><code>-XNoNPlusKPatterns</code></dt>
<dd> Disable support for n+k patterns [dynamic] </dd>
<dt><code>-XNoTraditionalRecordSyntax</code></dt>
<dd> Disable support for traditional record syntax (as supported by Haskell 98) C {f = x} [dynamic] </dd>
<dt><code>-XNoMonoPatBinds</code></dt>
<dd> Make pattern bindings polymorphic [dynamic] </dd>
<dt><code>-XRelaxedPolyRec</code></dt>
<dd> Relaxed checking for mutually-recursive polymorphic functions [dynamic] </dd>
<dt><code>-XExtendedDefaultRules</code></dt>
<dd> Use GHCi&#8217;s extended default rules in a normal module [dynamic] </dd>
<dt><code>-XOverloadedStrings</code></dt>
<dd> Enable overloaded string literals. [dynamic] </dd>
<dt><code>-XGADTs</code></dt>
<dd> Enable generalised algebraic data types. [dynamic] </dd>
<dt><code>-XGADTSyntax</code></dt>
<dd> Enable generalised algebraic data type syntax. [dynamic] </dd>
<dt><code>-XTypeFamilies</code></dt>
<dd> Enable type families. [dynamic] </dd>
<dt><code>-XConstraintKinds</code></dt>
<dd> Enable a kind of constraints. [dynamic] </dd>
<dt><code>-XDataKinds</code></dt>
<dd> Enable datatype promotion. [dynamic] </dd>
<dt><code>-XPolyKinds</code></dt>
<dd> Enable kind polymorphism. Implies <code>-XKindSignatures</code>. [dynamic] </dd>
<dt><code>-XScopedTypeVariables</code></dt>
<dd> Enable lexically-scoped type variables. Implied by <code>-fglasgow-exts</code>. [dynamic] </dd>
<dt><code>-XMonoLocalBinds</code></dt>
<dd> Enable do not generalise local bindings. [dynamic] </dd>
<dt><code>-XTemplateHaskell</code></dt>
<dd> Enable Template Haskell. No longer implied by <code>-fglasgow-exts</code>. [dynamic] </dd>
<dt><code>-XQuasiQuotes</code></dt>
<dd> Enable quasiquotation. [dynamic] </dd>
<dt><code>-XBangPatterns</code></dt>
<dd> Enable bang patterns. [dynamic] </dd>
<dt><code>-XCPP</code></dt>
<dd> Enable the C preprocessor. [dynamic] </dd>
<dt><code>-XPatternGuards</code></dt>
<dd> Enable pattern guards. [dynamic] </dd>
<dt><code>-XViewPatterns</code></dt>
<dd> Enable view patterns. [dynamic] </dd>
<dt><code>-XUnicodeSyntax</code></dt>
<dd> Enable unicode syntax. [dynamic] </dd>
<dt><code>-XMagicHash</code></dt>
<dd> Allow &quot;#&quot; as a postfix modifier on identifiers. [dynamic] </dd>
<dt><code>-XExplicitForAll</code></dt>
<dd> Enable explicit universal quantification. Implied by <code>-XScopedTypeVariables</code>, <code>-XLiberalTypeSynonyms</code>, <code>-XRank2Types</code>, <code>-XRankNTypes</code>, <code>-XPolymorphicComponents</code>, <code>-XExistentialQuantification</code> [dynamic] </dd>
<dt><code>-XPolymorphicComponents</code></dt>
<dd> Enable polymorphic components for data constructors. [dynamic] </dd>
<dt><code>-XRank2Types</code></dt>
<dd> Enable rank-2 types. [dynamic] </dd>
<dt><code>-XRankNTypes</code></dt>
<dd> Enable rank-N types. [dynamic] </dd>
<dt><code>-XImpredicativeTypes</code></dt>
<dd> Enable impredicative types. [dynamic] </dd>
<dt><code>-XExistentialQuantification</code></dt>
<dd> Enable existential quantification. [dynamic] </dd>
<dt><code>-XKindSignatures</code></dt>
<dd> Enable kind signatures. [dynamic] </dd>
<dt><code>-XEmptyDataDecls</code></dt>
<dd> Enable empty data declarations. [dynamic] </dd>
<dt><code>-XParallelListComp</code></dt>
<dd> Enable parallel list comprehensions. [dynamic] </dd>
<dt><code>-XTransformListComp</code></dt>
<dd> Enable generalised list comprehensions. [dynamic] </dd>
<dt><code>-XMonadComprehensions</code></dt>
<dd> Enable monad comprehensions. [dynamic] </dd>
<dt><code>-XUnliftedFFITypes</code></dt>
<dd> Enable unlifted FFI types. [dynamic] </dd>
<dt><code>-XInterruptibleFFI</code></dt>
<dd> Enable interruptible FFI. [dynamic] </dd>
<dt><code>-XLiberalTypeSynonyms</code></dt>
<dd> Enable liberalised type synonyms. [dynamic] </dd>
<dt><code>-XTypeOperators</code></dt>
<dd> Enable type operators. [dynamic] </dd>
<dt><code>-XExplicitNamespaces</code></dt>
<dd> Enable using the keyword type to specify the namespace of entries in imports and exports. [dynamic] </dd>
<dt><code>-XRecursiveDo</code></dt>
<dd> Enable recursive do (mdo) notation. [dynamic] </dd>
<dt><code>-XParallelArrays</code></dt>
<dd> Enable parallel arrays. [dynamic] </dd>
<dt><code>-XRecordWildCards</code></dt>
<dd> Enable record wildcards. [dynamic] </dd>
<dt><code>-XNamedFieldPuns</code></dt>
<dd> Enable record puns. [dynamic] </dd>
<dt><code>-XDisambiguateRecordFields</code></dt>
<dd> Enable record field disambiguation. [dynamic] </dd>
<dt><code>-XUnboxedTuples</code></dt>
<dd> Enable unboxed tuples. [dynamic] </dd>
<dt><code>-XStandaloneDeriving</code></dt>
<dd> Enable standalone deriving. [dynamic] </dd>
<dt><code>-XDeriveDataTypeable</code></dt>
<dd> Enable deriving for the Data and Typeable classes. [dynamic] </dd>
<dt><code>-XDeriveGeneric</code></dt>
<dd> Enable deriving for the Generic class. [dynamic] </dd>
<dt><code>-XGeneralizedNewtypeDeriving</code></dt>
<dd> Enable newtype deriving. [dynamic] </dd>
<dt><code>-XTypeSynonymInstances</code></dt>
<dd> Enable type synonyms in instance heads. [dynamic] </dd>
<dt><code>-XFlexibleContexts</code></dt>
<dd> Enable flexible contexts. [dynamic] </dd>
<dt><code>-XFlexibleInstances</code></dt>
<dd> Enable flexible instances. Implies <code>-XTypeSynonymInstances</code> [dynamic] </dd>
<dt><code>-XConstrainedClassMethods</code></dt>
<dd> Enable constrained class methods. [dynamic] </dd>
<dt><code>-XDefaultSignatures</code></dt>
<dd> Enable default signatures. [dynamic] </dd>
<dt><code>-XMultiParamTypeClasses</code></dt>
<dd> Enable multi parameter type classes. [dynamic] </dd>
<dt><code>-XFunctionalDependencies</code></dt>
<dd> Enable functional dependencies. [dynamic] </dd>
<dt><code>-XPackageImports</code></dt>
<dd> Enable package-qualified imports. [dynamic] </dd>
<dt><code>-XLambdaCase</code></dt>
<dd> Enable lambda-case expressions. [dynamic] </dd>
<dt><code>-XMultiWayIf</code></dt>
<dd> Enable multi-way if-expressions. [dynamic] </dd>
<dt><code>-XSafe</code></dt>
<dd> Enable the Safe Haskell Safe mode. [dynamic] </dd>
<dt><code>-XTrustworthy</code></dt>
<dd> Enable the Safe Haskell Trustworthy mode. [dynamic] </dd>
<dt><code>-XUnsafe</code></dt>
<dd> Enable Safe Haskell Unsafe mode. [dynamic] </dd>
<dt><code>-fpackage-trust</code></dt>
<dd> Enable Safe Haskell trusted package requirement for trustworty modules. [dynamic] </dd>
</dl>
<h2>WARNINGS</h2>
<dl>
<dt><code>-W</code></dt>
<dd> enable normal warnings [dynamic] </dd>
<dt><code>-w</code></dt>
<dd> disable all warnings [dynamic] </dd>
<dt><code>-Wall</code></dt>
<dd> enable almost all warnings (details in ) [dynamic] </dd>
<dt><code>-Werror</code></dt>
<dd> make warnings fatal [dynamic] </dd>
<dt><code>-Wwarn</code></dt>
<dd> make warnings non-fatal [dynamic] </dd>
<dt><code>-fdefer-type-errors</code></dt>
<dd> Defer as many type errors as possible until runtime. [dynamic] </dd>
<dt><code>-fhelpful-errors</code></dt>
<dd> Make suggestions for mis-spelled names. [dynamic] </dd>
<dt><code>-fwarn-deprecated-flags</code></dt>
<dd> warn about uses of commandline flags that are deprecated [dynamic] </dd>
<dt><code>-fwarn-duplicate-exports</code></dt>
<dd> warn when an entity is exported multiple times [dynamic] </dd>
<dt><code>-fwarn-hi-shadowing</code></dt>
<dd> warn when a .hi file in the current directory shadows a library [dynamic] </dd>
<dt><code>-fwarn-identities</code></dt>
<dd> warn about uses of Prelude numeric conversions that are probably the identity (and hence could be omitted) [dynamic] </dd>
<dt><code>-fwarn-implicit-prelude</code></dt>
<dd> warn when the Prelude is implicitly imported [dynamic] </dd>
<dt><code>-fwarn-incomplete-patterns</code></dt>
<dd> warn when a pattern match could fail [dynamic] </dd>
<dt><code>-fwarn-incomplete-uni-patterns</code></dt>
<dd> warn when a pattern match in a lambda expression or pattern binding could fail [dynamic] </dd>
<dt><code>-fwarn-incomplete-record-updates</code></dt>
<dd> warn when a record update could fail [dynamic] </dd>
<dt><code>-fwarn-lazy-unlifted-bindings</code></dt>
<dd> warn when a pattern binding looks lazy but must be strict [dynamic] </dd>
<dt><code>-fwarn-missing-fields</code></dt>
<dd> warn when fields of a record are uninitialised [dynamic] </dd>
<dt><code>-fwarn-missing-import-lists</code></dt>
<dd> warn when an import declaration does not explicitly list all the names brought into scope [dynamic] </dd>
<dt><code>-fwarn-missing-methods</code></dt>
<dd> warn when class methods are undefined [dynamic] </dd>
<dt><code>-fwarn-missing-signatures</code></dt>
<dd> warn about top-level functions without signatures [dynamic] </dd>
<dt><code>-fwarn-missing-local-sigs</code></dt>
<dd> warn about polymorphic local bindings without signatures [dynamic] </dd>
<dt><code>-fwarn-monomorphism-restriction</code></dt>
<dd> warn when the Monomorphism Restriction is applied [dynamic] </dd>
<dt><code>-fwarn-name-shadowing</code></dt>
<dd> warn when names are shadowed [dynamic] </dd>
<dt><code>-fwarn-orphans, -fwarn-auto-orphans</code></dt>
<dd> warn when the module contains orphan instance declarations or rewrite rules [dynamic] </dd>
<dt><code>-fwarn-overlapping-patterns</code></dt>
<dd> warn about overlapping patterns [dynamic] </dd>
<dt><code>-fwarn-tabs</code></dt>
<dd> warn if there are tabs in the source file [dynamic] </dd>
<dt><code>-fwarn-type-defaults</code></dt>
<dd> warn when defaulting happens [dynamic] </dd>
<dt><code>-fwarn-unrecognised-pragmas</code></dt>
<dd> warn about uses of pragmas that GHC doesn&#8217;t recognise [dynamic] </dd>
<dt><code>-fwarn-unused-binds</code></dt>
<dd> warn about bindings that are unused [dynamic] </dd>
<dt><code>-fwarn-unused-imports</code></dt>
<dd> warn about unnecessary imports [dynamic] </dd>
<dt><code>-fwarn-unused-matches</code></dt>
<dd> warn about variables in patterns that aren&#8217;t used [dynamic] </dd>
<dt><code>-fwarn-unused-do-bind</code></dt>
<dd> warn about do bindings that appear to throw away values of types other than () [dynamic] </dd>
<dt><code>-fwarn-wrong-do-bind</code></dt>
<dd> warn about do bindings that appear to throw away monadic values that you should have bound instead [dynamic] </dd>
<dt><code>-fwarn-unsafe</code></dt>
<dd> warn if the module being compiled is regarded to be unsafe. Should be used to check the safety status of modules when using safe inference. [dynamic] </dd>
<dt><code>-fwarn-safe</code></dt>
<dd> warn if the module being compiled is regarded to be safe. Should be used to check the safety status of modules when using safe inference. [dynamic] </dd>
<dt><code>-fwarn-warnings-deprecations</code></dt>
<dd> warn about uses of functions &amp; types that have warnings or deprecated pragmas [dynamic] </dd>
</dl>
<h2>OPTIMISATION LEVELS</h2>
<dl>
<dt><code>-O</code></dt>
<dd> Enable default optimisation (level 1) [dynamic] </dd>
<dt><code>-O</code><i>n</i></dt>
<dd> Set optimisation level <i>n</i> [dynamic] </dd>
</dl>
<h2>INDIVIDUAL OPTIMISATIONS</h2>
<dl>
<dt><code>-fcase-merge</code></dt>
<dd> Enable case-merging. Implied by <code>-O</code>. [dynamic] </dd>
<dt><code>-fcse</code></dt>
<dd> Turn on common sub-expression elimination. Implied by <code>-O</code>. [dynamic] </dd>
<dt><code>-fdicts-strict</code></dt>
<dd> Make dictionaries strict [static] </dd>
<dt><code>-fdo-eta-reduction</code></dt>
<dd> Enable eta-reduction. Implied by <code>-O</code>. [dynamic] </dd>
<dt><code>-fdo-lambda-eta-expansion</code></dt>
<dd> Enable lambda eta-reduction [dynamic] </dd>
<dt><code>-feager-blackholing</code></dt>
<dd> Turn on eager blackholing [dynamic] </dd>
<dt><code>-fenable-rewrite-rules</code></dt>
<dd> Switch on all rewrite rules (including rules generated by automatic specialisation of overloaded functions). Implied by <code>-O</code>. [dynamic] </dd>
<dt><code>-fvectorise</code></dt>
<dd> Enable vectorisation of nested data parallelism [dynamic] </dd>
<dt><code>-favoid-vect</code></dt>
<dd> Enable vectorisation avoidance (EXPERIMENTAL) [dynamic] </dd>
<dt><code>-fexcess-precision</code></dt>
<dd> Enable excess intermediate precision [dynamic] </dd>
<dt><code>-ffloat-in</code></dt>
<dd> Turn on the float-in transformation. Implied by <code>-O</code>. [dynamic] </dd>
<dt><code>-ffull-laziness</code></dt>
<dd> Turn on full laziness (floating bindings outwards). Implied by <code>-O</code>. [dynamic] </dd>
<dt><code>-fignore-asserts</code></dt>
<dd> Ignore assertions in the source [dynamic] </dd>
<dt><code>-fignore-interface-pragmas</code></dt>
<dd> Ignore pragmas in interface files [dynamic] </dd>
<dt><code>-fliberate-case</code></dt>
<dd> Turn on the liberate-case transformation. Implied by <code>-O2</code>. [dynamic] </dd>
<dt><code>-fliberate-case-threshold</code>=<i>n</i></dt>
<dd> Set the size threshold for the liberate-case transformation to <i>n</i> (default: 200) [static] </dd>
<dt><code>-fmax-simplifier-iterations</code></dt>
<dd> Set the max iterations for the simplifier [dynamic] </dd>
<dt><code>-fmax-worker-args</code></dt>
<dd> If a worker has that many arguments, none will be unpacked anymore (default: 10) [static] </dd>
<dt><code>-fno-opt-coercion</code></dt>
<dd> Turn off the coercion optimiser [static] </dd>
<dt><code>-fno-pre-inlining</code></dt>
<dd> Turn off pre-inlining [static] </dd>
<dt><code>-fno-state-hack</code></dt>
<dd> Turn off the &quot;state hack&quot; whereby any lambda with a real-world state token as argument is considered to be single-entry. Hence OK to inline things inside it. [static] </dd>
<dt><code>-fpedantic-bottoms</code></dt>
<dd> Make GHC be more precise about its treatment of bottom (but see also <code>-fno-state-hack</code>). In particular, GHC will not eta-expand through a case expression. [dynamic] </dd>
<dt><code>-fomit-interface-pragmas</code></dt>
<dd> Don&#8217;t generate interface pragmas [dynamic] </dd>
<dt><code>-fsimplifier-phases</code></dt>
<dd> Set the number of phases for the simplifier (default 2). Ignored with <code>-O0</code>. [dynamic] </dd>
<dt><code>-fsimpl-tick-factor=n</code></dt>
<dd> Set the percentage factor for simplifier ticks (default 100) [dynamic] </dd>
<dt><code>-fspec-constr</code></dt>
<dd> Turn on the SpecConstr transformation. Implied by <code>-O2</code>. [dynamic] </dd>
<dt><code>-fspec-constr-threshold</code>=<i>n</i></dt>
<dd> Set the size threshold for the SpecConstr transformation to <i>n</i> (default: 200) [static] </dd>
<dt><code>-fspec-constr-count</code>=<i>n</i></dt>
<dd> Set to <i>n</i> (default: 3) the maximum number of specialisations that will be created for any one function by the SpecConstr transformation [static] </dd>
<dt><code>-fspecialise</code></dt>
<dd> Turn on specialisation of overloaded functions. Implied by <code>-O</code>. [dynamic] </dd>
<dt><code>-fstrictness</code></dt>
<dd> Turn on strictness analysis. Implied by <code>-O</code>. [dynamic] </dd>
<dt><code>-fstrictness=before</code>=<i>n</i></dt>
<dd> Run an additional strictness analysis before simplifier phase <i>n</i> [dynamic] </dd>
<dt><code>-fstatic-argument-transformation</code></dt>
<dd> Turn on the static argument transformation. Implied by <code>-O2</code>. [dynamic] </dd>
<dt><code>-funbox-strict-fields</code></dt>
<dd> Flatten strict constructor fields [dynamic] </dd>
<dt><code>-funfolding-creation-threshold</code></dt>
<dd> Tweak unfolding settings [static] </dd>
<dt><code>-funfolding-fun-discount</code></dt>
<dd> Tweak unfolding settings [static] </dd>
<dt><code>-funfolding-keeness-factor</code></dt>
<dd> Tweak unfolding settings [static] </dd>
<dt><code>-funfolding-use-threshold</code></dt>
<dd> Tweak unfolding settings [static] </dd>
</dl>
<h2>PROFILING OPTIONS</h2>
<dl>
<dt><code>-prof</code></dt>
<dd> Turn on profiling [static] </dd>
<dt><code>-fprof-auto</code></dt>
<dd> Auto-add SCCs to all bindings not marked INLINE [dynamic] </dd>
<dt><code>-fprof-auto-top</code></dt>
<dd> Auto-add SCCs to all top-level bindings not marked INLINE [dynamic] </dd>
<dt><code>-fprof-auto-exported</code></dt>
<dd> Auto-add SCCs to all exported bindings not marked INLINE [dynamic] </dd>
<dt><code>-fprof-cafs</code></dt>
<dd> Auto-add SCCs to all CAFs [dynamic] </dd>
<dt><code>-fno-prof-count-entries</code></dt>
<dd> Do not collect entry counts [dynamic] </dd>
<dt><code>-ticky</code></dt>
<dd> Turn on ticky-ticky profiling [static] </dd>
</dl>
<h2>PROGRAM COVERAGE OPTIONS</h2>
<dl>
<dt><code>-fhpc</code></dt>
<dd> Turn on Haskell program coverage instrumentation [static] </dd>
<dt><code>-hpcdir dir</code></dt>
<dd> Directory to deposit .mix files during compilation (default is .hpc) [dynamic] </dd>
</dl>
<h2>HASKELL PRE-PROCESSOR OPTIONS</h2>
<dl>
<dt><code>-F</code></dt>
<dd> Enable the use of a pre-processor (set with <code>-pgmF</code>) [dynamic] </dd>
</dl>
<h2>C PRE-PROCESSOR OPTIONS</h2>
<dl>
<dt><code>-cpp</code></dt>
<dd> Run the C pre-processor on Haskell source files [dynamic] </dd>
<dt><code>-D</code><i>symbol</i>=<i>value</i></dt>
<dd> Define a symbol in the C pre-processor [dynamic] </dd>
<dt><code>-U</code><i>symbol</i></dt>
<dd> Undefine a symbol in the C pre-processor [dynamic] </dd>
<dt><code>-I</code><i>dir</i></dt>
<dd> Add <i>dir</i> to the directory search list for #include files [dynamic] </dd>
</dl>
<h2>CODE GENERATION OPTIONS</h2>
<dl>
<dt><code>-fasm</code></dt>
<dd> Use the native code generator [dynamic] </dd>
<dt><code>-fllvm</code></dt>
<dd> Compile using the LLVM code generator [dynamic] </dd>
<dt><code>-fno-code</code></dt>
<dd> Omit code generation [dynamic] </dd>
<dt><code>-fbyte-code</code></dt>
<dd> Generate byte-code [dynamic] </dd>
<dt><code>-fobject-code</code></dt>
<dd> Generate object code [dynamic] </dd>
</dl>
<h2>LINKING OPTIONS</h2>
<dl>
<dt><code>-shared</code></dt>
<dd> Generate a shared library (as opposed to an executable) [dynamic] </dd>
<dt><code>-fPIC</code></dt>
<dd> Generate position-independent code (where available) [static] </dd>
<dt><code>-dynamic</code></dt>
<dd> Use dynamic Haskell libraries (if available) [static] </dd>
<dt><code>-dynload</code></dt>
<dd> Selects one of a number of modes for finding shared libraries at runtime. [static] </dd>
<dt><code>-framework</code> <i>name</i></dt>
<dd> On Darwin/MacOS X only, link in the framework <i>name</i>. This option corresponds to the <code>-framework</code> option for Apple&#8217;s Linker. [dynamic] </dd>
<dt><code>-framework-path</code> <i>name</i></dt>
<dd> On Darwin/MacOS X only, add <i>dir</i> to the list of directories searched for frameworks. This option corresponds to the <code>-F</code> option for Apple&#8217;s Linker. [dynamic] </dd>
<dt><code>-l</code><i>lib</i></dt>
<dd> Link in library <i>lib</i> [dynamic] </dd>
<dt><code>-L</code><i>dir</i></dt>
<dd> Add <i>dir</i> to the list of directories searched for libraries [dynamic] </dd>
<dt><code>-main-is</code></dt>
<dd> Set main module and function [dynamic] </dd>
<dt><code>&#8211;mk-dll</code></dt>
<dd> DLL-creation mode (Windows only) [dynamic] </dd>
<dt><code>-no-hs-main</code></dt>
<dd> Don&#8217;t assume this program contains main [dynamic] </dd>
<dt><code>-rtsopts</code>, <code>-rtsopts={none,some,all}</code></dt>
<dd> Control whether the RTS behaviour can be tweaked via command-line flags and the GHCRTS environment variable. Using none means no RTS flags can be given; some means only a minimum of safe options can be given (the default), and all (or no argument at all) means that all RTS flags are permitted. [dynamic] </dd>
<dt><code>-with-rtsopts=opts</code></dt>
<dd> Set the default RTS options to <i>opts</i>. [dynamic] </dd>
<dt><code>-no-link</code></dt>
<dd> Omit linking [dynamic] </dd>
<dt><code>-split-objs</code></dt>
<dd> Split objects (for libraries) [dynamic] </dd>
<dt><code>-static</code></dt>
<dd> Use static Haskell libraries [static] </dd>
<dt><code>-threaded</code></dt>
<dd> Use the threaded runtime [static] </dd>
<dt><code>-debug</code></dt>
<dd> Use the debugging runtime [static] </dd>
<dt><code>-eventlog</code></dt>
<dd> Enable runtime event tracing [static] </dd>
<dt><code>-fno-gen-manifest</code></dt>
<dd> Do not generate a manifest file (Windows only) [dynamic] </dd>
<dt><code>-fno-embed-manifest</code></dt>
<dd> Do not embed the manifest in the executable (Windows only) [dynamic] </dd>
<dt><code>-fno-shared-implib</code></dt>
<dd> Don&#8217;t generate an import library for a DLL (Windows only) [dynamic] </dd>
<dt><code>-dylib-install-name</code> <i>path</i></dt>
<dd> Set the install name (via -install_name passed to Apple&#8217;s linker), specifying the full install path of the library file. Any libraries or executables that link with it later will pick up that path as their runtime search location for it. (Darwin/MacOS X only) [dynamic] </dd>
</dl>
<h2>PLUGIN OPTIONS</h2>
<dl>
<dt><code>-fplugin</code>=<i>module</i></dt>
<dd> Load a plugin exported by a given module [static] </dd>
<dt><code>-fplugin-opt</code>=<i>module:args</i></dt>
<dd> Give arguments to a plugin module; module must be specified with <code>-fplugin</code> [static] </dd>
</dl>
<h2>REPLACING PHASES</h2>
<dl>
<dt><code>-pgmL</code> <i>cmd</i></dt>
<dd> Use <i>cmd</i> as the literate pre-processor [dynamic] </dd>
<dt><code>-pgmP</code> <i>cmd</i></dt>
<dd> Use <i>cmd</i> as the C pre-processor (with <code>-cpp</code> only) [dynamic] </dd>
<dt><code>-pgmc</code> <i>cmd</i></dt>
<dd> Use <i>cmd</i> as the C compiler [dynamic] </dd>
<dt><code>-pgms</code> <i>cmd</i></dt>
<dd> Use <i>cmd</i> as the splitter [dynamic] </dd>
<dt><code>-pgma</code> <i>cmd</i></dt>
<dd> Use <i>cmd</i> as the assembler [dynamic] </dd>
<dt><code>-pgml</code> <i>cmd</i></dt>
<dd> Use <i>cmd</i> as the linker [dynamic] </dd>
<dt><code>-pgmdll</code> <i>cmd</i></dt>
<dd> Use <i>cmd</i> as the DLL generator [dynamic] </dd>
<dt><code>-pgmF</code> <i>cmd</i></dt>
<dd> Use <i>cmd</i> as the pre-processor (with <code>-F</code> only) [dynamic] </dd>
<dt><code>-pgmwindres</code> <i>cmd</i></dt>
<dd> Use <i>cmd</i> as the program for embedding manifests on Windows. [dynamic] </dd>
</dl>
<h2>FORCING OPTIONS TO PARTICULAR PHASES</h2>
<dl>
<dt><code>-optL</code> <i>option</i></dt>
<dd> pass <i>option</i> to the literate pre-processor [dynamic] </dd>
<dt><code>-optP</code> <i>option</i></dt>
<dd> pass <i>option</i> to cpp (with <code>-cpp</code> only) [dynamic] </dd>
<dt><code>-optF</code> <i>option</i></dt>
<dd> pass <i>option</i> to the custom pre-processor [dynamic] </dd>
<dt><code>-optc</code> <i>option</i></dt>
<dd> pass <i>option</i> to the C compiler [dynamic] </dd>
<dt><code>-optlo</code> <i>option</i></dt>
<dd> pass <i>option</i> to the LLVM optimiser [dynamic] </dd>
<dt><code>-optlc</code> <i>option</i></dt>
<dd> pass <i>option</i> to the LLVM compiler [dynamic] </dd>
<dt><code>-optm</code> <i>option</i></dt>
<dd> pass <i>option</i> to the mangler [dynamic] </dd>
<dt><code>-opta</code> <i>option</i></dt>
<dd> pass <i>option</i> to the assembler [dynamic] </dd>
<dt><code>-optl</code> <i>option</i></dt>
<dd> pass <i>option</i> to the linker [dynamic] </dd>
<dt><code>-optdll</code> <i>option</i></dt>
<dd> pass <i>option</i> to the DLL generator [dynamic] </dd>
<dt><code>-optwindres</code> <i>option</i></dt>
<dd> pass <i>option</i> to windres. [dynamic] </dd>
</dl>
<h2>PLATFORM-SPECIFIC OPTIONS</h2>
<dl>
<dt><code>-msse2</code></dt>
<dd> (x86 only) Use SSE2 for floating point [dynamic] </dd>
<dt><code>-monly-[432]-regs</code></dt>
<dd> (x86 only) give some registers back to the C compiler [dynamic] </dd>
</dl>
<h2>EXTERNAL CORE FILE OPTIONS</h2>
<dl>
<dt><code>-fext-core</code></dt>
<dd> Generate .hcr external Core files [dynamic] </dd>
</dl>
<h2>COMPILER DEBUGGING OPTIONS</h2>
<dl>
<dt><code>-dcore-lint</code></dt>
<dd> Turn on internal sanity checking [dynamic] </dd>
<dt><code>-ddump-to-file</code></dt>
<dd> Dump to files instead of stdout [dynamic] </dd>
<dt><code>-ddump-asm</code></dt>
<dd> Dump assembly [dynamic] </dd>
<dt><code>-ddump-bcos</code></dt>
<dd> Dump interpreter byte code [dynamic] </dd>
<dt><code>-ddump-cmm</code></dt>
<dd> Dump C&#8211; output [dynamic] </dd>
<dt><code>-ddump-core-stats</code></dt>
<dd> Print a one-line summary of the size of the Core program at the end of the optimisation pipeline [dynamic] </dd>
<dt><code>-ddump-cpranal</code></dt>
<dd> Dump output from CPR analysis [dynamic] </dd>
<dt><code>-ddump-cse</code></dt>
<dd> Dump CSE output [dynamic] </dd>
<dt><code>-ddump-deriv</code></dt>
<dd> Dump deriving output [dynamic] </dd>
<dt><code>-ddump-ds</code></dt>
<dd> Dump desugarer output [dynamic] </dd>
<dt><code>-ddump-flatC</code></dt>
<dd> Dump `flat&#8217; C [dynamic] </dd>
<dt><code>-ddump-foreign</code></dt>
<dd> Dump foreign export stubs [dynamic] </dd>
<dt><code>-ddump-hpc</code></dt>
<dd> Dump after instrumentation for program coverage [dynamic] </dd>
<dt><code>-ddump-inlinings</code></dt>
<dd> Dump inlining info [dynamic] </dd>
<dt><code>-ddump-llvm</code></dt>
<dd> Dump LLVM intermediate code [dynamic] </dd>
<dt><code>-ddump-occur-anal</code></dt>
<dd> Dump occurrence analysis output [dynamic] </dd>
<dt><code>-ddump-opt-cmm</code></dt>
<dd> Dump the results of C&#8211; to C&#8211; optimising passes [dynamic] </dd>
<dt><code>-ddump-parsed</code></dt>
<dd> Dump parse tree [dynamic] </dd>
<dt><code>-ddump-prep</code></dt>
<dd> Dump prepared core [dynamic] </dd>
<dt><code>-ddump-rn</code></dt>
<dd> Dump renamer output [dynamic] </dd>
<dt><code>-ddump-rule-firings</code></dt>
<dd> Dump rule firing info [dynamic] </dd>
<dt><code>-ddump-rule-rewrites</code></dt>
<dd> Dump detailed rule firing info [dynamic] </dd>
<dt><code>-ddump-rules</code></dt>
<dd> Dump rules [dynamic] </dd>
<dt><code>-ddump-vect</code></dt>
<dd> Dump vectoriser input and output [dynamic] </dd>
<dt><code>-ddump-simpl</code></dt>
<dd> Dump final simplifier output [dynamic] </dd>
<dt><code>-ddump-simpl-phases</code></dt>
<dd> Dump output from each simplifier phase [dynamic] </dd>
<dt><code>-ddump-simpl-iterations</code></dt>
<dd> Dump output from each simplifier iteration [dynamic] </dd>
<dt><code>-ddump-spec</code></dt>
<dd> Dump specialiser output [dynamic] </dd>
<dt><code>-ddump-splices</code></dt>
<dd> Dump TH spliced expressions, and what they evaluate to [dynamic] </dd>
<dt><code>-ddump-stg</code></dt>
<dd> Dump final STG [dynamic] </dd>
<dt><code>-ddump-stranal</code></dt>
<dd> Dump strictness analyser output [dynamic] </dd>
<dt><code>-ddump-tc</code></dt>
<dd> Dump typechecker output [dynamic] </dd>
<dt><code>-ddump-types</code></dt>
<dd> Dump type signatures [dynamic] </dd>
<dt><code>-ddump-worker-wrapper</code></dt>
<dd> Dump worker-wrapper output [dynamic] </dd>
<dt><code>-ddump-if-trace</code></dt>
<dd> Trace interface files [dynamic] </dd>
<dt><code>-ddump-tc-trace</code></dt>
<dd> Trace typechecker [dynamic] </dd>
<dt><code>-ddump-vt-trace</code></dt>
<dd> Trace vectoriser [dynamic] </dd>
<dt><code>-ddump-rn-trace</code></dt>
<dd> Trace renamer [dynamic] </dd>
<dt><code>-ddump-rn-stats</code></dt>
<dd> Renamer stats [dynamic] </dd>
<dt><code>-ddump-simpl-stats</code></dt>
<dd> Dump simplifier stats [dynamic] </dd>
<dt><code>-dno-debug-output</code></dt>
<dd> Suppress unsolicited debugging output [static] </dd>
<dt><code>-dppr-debug</code></dt>
<dd> Turn on debug printing (more verbose) [static] </dd>
<dt><code>-dppr-noprags</code></dt>
<dd> Don&#8217;t output pragma info in dumps [static] </dd>
<dt><code>-dppr-user-length</code></dt>
<dd> Set the depth for printing expressions in error msgs [dynamic] </dd>
<dt><code>-dppr-colsNNN</code></dt>
<dd> Set the width of debugging output. For example <code>-dppr-cols200</code> [dynamic] </dd>
<dt><code>-dppr-case-as-let</code></dt>
<dd> Print single alternative case expressions as strict lets. [dynamic] </dd>
<dt><code>-dsuppress-all</code></dt>
<dd> In core dumps, suppress everything that is suppressable. [static] </dd>
<dt><code>-dsuppress-uniques</code></dt>
<dd> Suppress the printing of uniques in debug output (easier to use diff) [static] </dd>
<dt><code>-dsuppress-idinfo</code></dt>
<dd> Suppress extended information about identifiers where they are bound [static] </dd>
<dt><code>-dsuppress-module-prefixes</code></dt>
<dd> Suppress the printing of module qualification prefixes [static] </dd>
<dt><code>-dsuppress-type-signatures</code></dt>
<dd> Suppress type signatures [static] </dd>
<dt><code>-dsuppress-type-applications</code></dt>
<dd> Suppress type applications [static] </dd>
<dt><code>-dsuppress-coercions</code></dt>
<dd> Suppress the printing of coercions in Core dumps to make them shorter [static] </dd>
<dt><code>-dsource-stats</code></dt>
<dd> Dump haskell source stats [dynamic] </dd>
<dt><code>-dcmm-lint</code></dt>
<dd> C&#8211; pass sanity checking [dynamic] </dd>
<dt><code>-dstg-lint</code></dt>
<dd> STG pass sanity checking [dynamic] </dd>
<dt><code>-dstg-stats</code></dt>
<dd> Dump STG stats [dynamic] </dd>
<dt><code>-dverbose-core2core</code></dt>
<dd> Show output from each core-to-core pass [dynamic] </dd>
<dt><code>-dverbose-stg2stg</code></dt>
<dd> Show output from each STG-to-STG pass [dynamic] </dd>
<dt><code>-dshow-passes</code></dt>
<dd> Print out each pass name as it happens [dynamic] </dd>
<dt><code>-dfaststring-stats</code></dt>
<dd> Show statistics for fast string usage when finished [dynamic] </dd>
</dl>
<h2>MISC COMPILER OPTIONS</h2>
<dl>
<dt><code>-fno-hi-version-check</code></dt>
<dd> Don&#8217;t complain about .hi file mismatches [static] </dd>
<dt><code>-dno-black-holing</code></dt>
<dd> Turn off black holing (probably doesn&#8217;t work) [static] </dd>
<dt><code>-fhistory-size</code></dt>
<dd> Set simplification history size [static] </dd>
<dt><code>-funregisterised</code></dt>
<dd> Unregisterised compilation (use <code>-unreg</code> instead) [static] </dd>
<dt><code>-fno-ghci-history</code></dt>
<dd> Do not use the load/store the GHCi command history from/to ghci_history. [dynamic] </dd>
<dt><code>-fno-ghci-sandbox</code></dt>
<dd> Turn off the GHCi sandbox. Means computations are run in the main thread, rather than a forked thread. [dynamic] </dd>
</dl>
<h2>FILES</h2>
<p> <i>/usr/lib64</i> </p>
<h2>COPYRIGHT</h2>
<p> Copyright 2002, The University Court of the University of Glasgow.<br />
 All rights reserved. </p>
<h2>AUTHOR</h2>
<p> This manual page was generated from the XML documentation of GHC with blood, sweat, tears and a breaks-if-you-look-at-it-the-wrong-way XSL stylesheet originally written by Michael Weber &lt;michaelw [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
