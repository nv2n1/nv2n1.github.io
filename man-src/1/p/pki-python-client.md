---
title: "pki-python-client(1)"
name: "pki-python-client"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-python-client/"
description: "pki-python-client – Dogtag Python Client API"
---

<h2>NAME</h2>
<p> pki-python-client &#8211; Dogtag Python Client API </p>
<p> Dogtag is an enterprise software system designed to manage enterprise Public Key Infrastructure (PKI) deployments. These pages document the Python client API that can be used to interact with Dogtag&#8217;s REST API to request and issue certificates, store secrets in the KRA etc.</p>
<h2>PKI PACKAGE</h2>
<h3><code>pki</code> Package</h3>
<p> This module contains top-level classes and functions used by the Dogtag project.</p>
<dl>
<dt><code>class pki.Attribute(name, value)</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class representing a key/value pair. </p>
<p> This object is the basis of the representation of a ResourceMessage.</p>
<dt><code>class pki.AttributeList</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class representing a list of attributes. </p>
<p> This class is needed because of a JavaMapper used in the REST API.</p>
<dt><code>exception pki.BadRequestException(message, exception=None, code=None, class_name=None)</code></p>
<dd> Bases: <code>pki.PKIException</code> </p>
<p> Bad Request Exception: return code = 400</p>
<dt><code>exception pki.CertNotFoundException(message, exception=None, code=None, class_name=None)</code></p>
<dd> Bases: <code>pki.ResourceNotFoundException</code> </p>
<p> Cert Not Found Exception: return code = 404</p>
<dt><code>exception pki.ConflictingOperationException(message, exception=None, code=None, class_name=None)</code></p>
<dd> Bases: <code>pki.PKIException</code> </p>
<p> Conflicting Operation Exception: return code = 409</p>
<dt><code>exception pki.ForbiddenException(message, exception=None, code=None, class_name=None)</code></p>
<dd> Bases: <code>pki.PKIException</code> </p>
<p> Forbidden Exception: return code = 403</p>
<dt><code>exception pki.GroupNotFoundException(message, exception=None, code=None, class_name=None)</code></p>
<dd> Bases: <code>pki.ResourceNotFoundException</code> </p>
<p> Group Not Found Exception: return code = 404</p>
<dt><code>exception pki.HTTPGoneException(message, exception=None, code=None, class_name=None)</code></p>
<dd> Bases: <code>pki.PKIException</code> </p>
<p> Gone Exception: return code = 410</p>
<dt><code>exception pki.KeyNotFoundException(message, exception=None, code=None, class_name=None)</code></p>
<dd> Bases: <code>pki.ResourceNotFoundException</code> </p>
<p> Key Not Found Exception: return code 404</p>
<dt><code>class pki.Link</code></p>
<dd> Bases: <code>object</code> </p>
<p> Stores the information of the resteasy&#8217;s Link object sent by the server for a resource.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd> Generate Link from JSON</p>
<dt><code>Parameters</code></p>
<dd> <code>attr_list</code> (<i>str</i>) &#8212; JSON representation of Link</p>
<dt><code>Returns</code></p>
<dd> pki.Link</p>
<dt><code>exception pki.PKIException(message, exception=None, code=None, class_name=None)</code></p>
<dd> Bases: <code>exceptions.Exception</code>, <code>pki.ResourceMessage</code> </p>
<p> Base exception class for REST Interface</p>
<dt><code>classmethod from_json(json_value)</code></p>
<dd> Construct PKIException from JSON. :param json_value: JSON representation of the exception. :type json_value: str :return: pki.PKIException</p>
<dt><code>exception pki.ProfileNotFoundException(message, exception=None, code=None, class_name=None)</code></p>
<dd> Bases: <code>pki.ResourceNotFoundException</code> </p>
<p> Profile Not Found Exception: return code = 404</p>
<dt><code>class pki.PropertyFile(filename, delimiter=&#8217;=&#8217;)</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class to manage property files The contents of the property file are maintained internally as a list of properties. </p>
<p> Properties are strings of the format &lt;name&gt; &lt;delimiter&gt; &lt;value&gt; where &#8216;=&#8217; is the default delimiter.</p>
<dt><code>get(name)</code></p>
<dd> Get the value of the specified property.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> (<i>str</i>) &#8212; name of property to be fetched.</p>
<dt><code>Returns</code></p>
<dd> str &#8212; value of property</p>
<dt><code>index(name)</code></p>
<dd> Find the index (position) of a property in a property file.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> (<i>str</i>) &#8212; name of property</p>
<dt><code>Returns</code></p>
<dd> int &#8212; index of property.</p>
<dt><code>insert_line(index, line)</code></p>
<dd> Insert property into the list of properties maintained by this object at the specified location (index).</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>index</code> (<i>int</i>) &#8212; point at which to insert value.</p>
<dt>&bull;</p>
<dd> <code>line</code> (<i>str</i>) &#8212; value to be inserted.</p>
<dt><code>Returns</code></p>
<dd> None</p>
<dt><code>read()</code></p>
<dd> Read from property file into the list of properties maintained by this object.</p>
<dt><code>Returns</code></p>
<dd> None</p>
<dt><code>remove(name)</code></p>
<dd> Remove property from list of properties maintained by this object.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> (<i>str</i>) &#8212; name of property to be removed.</p>
<dt><code>Returns</code></p>
<dd> None</p>
<dt><code>remove_line(index)</code></p>
<dd> Remove property at specified index from the properties list.</p>
<dt><code>Parameters</code></p>
<dd> <code>index</code> (<i>int</i>) &#8212; location of property to be removed.</p>
<dt><code>Returns</code></p>
<dd> None</p>
<dt><code>set(name, value, index=None)</code></p>
<dd> Set value of specified property.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> (<i>str</i>) &#8212; name of property to set.</p>
<dt>&bull;</p>
<dd> <code>value</code> (<i>str</i>) &#8212; value to set</p>
<dt>&bull;</p>
<dd> <code>index</code> (<i>int</i>) &#8212; (optional) position of property</p>
<dt><code>Returns</code></p>
<dd> None</p>
<dt><code>show()</code></p>
<dd> Print the contents of the list of properties maintained by this object to STDOUT.</p>
<dt><code>Returns</code></p>
<dd> None</p>
<dt><code>write()</code></p>
<dd> Write the list of properties maintained by this object to the property file.</p>
<dt><code>Returns</code></p>
<dd> None</p>
<dt><code>exception pki.RequestNotFoundException(message, exception=None, code=None, class_name=None)</code></p>
<dd> Bases: <code>pki.ResourceNotFoundException</code> </p>
<p> Request Not Found Exception: return code = 404</p>
<dt><code>class pki.ResourceMessage(class_name)</code></p>
<dd> Bases: <code>object</code> </p>
<p> This class is the basis for the various types of key requests. It is essentially a list of attributes.</p>
<dt><code>add_attribute(name, value)</code></p>
<dd> Add an attribute to the list.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>name</code> (<i>str</i>) &#8212; name of attribute to add</p>
<dt>&bull;</p>
<dd> <code>value</code> (<i>str</i>) &#8212; value to add</p>
<dt><code>Returns</code></p>
<dd> None</p>
<dt><code>get_attribute_value(name)</code></p>
<dd> Get the value of a given attribute.</p>
<dt><code>Parameters</code></p>
<dd> <code>name</code> (<i>str</i>) &#8212; name of attribute to retrieve</p>
<dt><code>Returns</code></p>
<dd> str &#8212; value of parameter</p>
<dt><code>exception pki.ResourceNotFoundException(message, exception=None, code=None, class_name=None)</code></p>
<dd> Bases: <code>pki.PKIException</code> </p>
<p> Not Found Exception: return code = 404</p>
<dt><code>exception pki.UnauthorizedException(message, exception=None, code=None, class_name=None)</code></p>
<dd> Bases: <code>pki.PKIException</code> </p>
<p> Unauthorized Exception: return code = 401</p>
<dt><code>exception pki.UserNotFoundException(message, exception=None, code=None, class_name=None)</code></p>
<dd> Bases: <code>pki.ResourceNotFoundException</code> </p>
<p> User Not Found Exception: return code = 404</p>
<dt><code>pki.handle_exceptions()</code></p>
<dd> Decorator handling exceptions from REST methods.</p>
<dt><code>pki.implementation_version()</code></p>
<dd> Return implementation version.</p>
<dt><code>Returns</code></p>
<dd> str &#8211;implementation version</p>
<dt><code>pki.read_text(message, options=None, default=None, delimiter=&#8217;:&#8217;, allow_empty=True, case_sensitive=True)</code></p>
<dd> Get an input from the user. This is used, for example, in pkispawn and pkidestroy to obtain user input.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>message</code> (<i>str</i>) &#8212; prompt to display to the user</p>
<dt>&bull;</p>
<dd> <code>options</code> (<i>list</i>) &#8212; list of possible inputs by the user.</p>
<dt>&bull;</p>
<dd> <code>default</code> (<i>str</i>) &#8212; default value of parameter being prompted.</p>
<dt>&bull;</p>
<dd> <code>delimiter</code> (<i>str</i>) &#8212; delimiter to be used at the end of the prompt.</p>
<dt>&bull;</p>
<dd> <code>allow_empty</code> (<i>boolean &#8212; True/False</i>) &#8212; Allow input to be empty.</p>
<dt>&bull;</p>
<dd> <code>case_sensitive</code> (<i>boolean &#8212; True/False</i>) &#8212; Allow input to be case sensitive.</p>
<dt><code>Returns</code></p>
<dd> str &#8212; value obtained from user input.</dl>
<h3><code>account</code> Module</h3>
<dl>
<dt><code>class pki.account.AccountClient(connection)</code></p>
<dd> Class used to associate an authentication session variable with a connection.</p>
<dt><code>To use this class:</code></p>
<dd>
<dt>&bull;</p>
<dd> set the authentication credentials with the connection,</p>
<dt>&bull;</p>
<dd> create an AccountClient and then call login().</p>
<dt>&bull;</p>
<dd> further operations in this session will use the same authentication credentials without re-authentication.</p>
<dt>&bull;</p>
<dd> call logout() to invalidate the session.</p>
<dt><code>login(inst, *args, **kwargs)</code></p>
<dd> Login to account REST interface. If login is successful, an authentication session variable is associated with the connection.</p>
<dt><code>Returns</code></p>
<dd> None</p>
<dt><code>logout(inst, *args, **kwargs)</code></p>
<dd> Logs out of the session. Authentication session variables are invalidated for the connection</p>
<dt><code>Returns</code></p>
<dd> None</dl>
<h3><code>cert</code> Module</h3>
<dl>
<dt><code>class pki.cert.CertClient(connection)</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class encapsulating and mirroring the functionality in the CertResource Java interface class defining the REST API for Certificate resources.</p>
<dt><code>approve_request(request_id, cert_review_response=None)</code></p>
<dd> Approves a certificate enrollment request. If cert_review_response is None, a review request operation is performed to fetch the CertReviewResponse object. Requires as agent level authentication.</p>
<dt><code>assign_request(request_id, cert_review_response)</code></p>
<dd> Assigns a certificate enrollment request. If cert_review_response is None, a review request operation is performed to fetch the CertReviewResponse object. Requires as agent level authentication.</p>
<dt><code>cancel_request(request_id, cert_review_response=None)</code></p>
<dd> Cancels a certificate enrollment request. If cert_review_response is None, a review request operation is performed to fetch the CertReviewResponse object. Requires as agent level authentication.</p>
<dt><code>create_enrollment_request(inst, *args, **kwargs)</code></p>
<dd> Fetches the enrollment request object for the given profile and sets values to its attributes using the values provided in the inputs dictionary. Returns the CertEnrollmentRequest object, which can be submitted to enroll a certificate.</p>
<dt><code>enroll_cert(inst, *args, **kwargs)</code></p>
<dd> A convenience method for enrolling a certificate for a given profile id. The inputs parameter should be a dictionary with values for the profile attributes for an enrollment request. </p>
<p> Calling this method with valid arguments, creates an enrollment request, submits it to the server, approves the certificate requests generated for the enrollment and returns a list of CertData objects for all the certificates generated as part of this enrollment. </p>
<p> Note: This method supports only certificate enrollment where only one agent approval is sufficient. </p>
<p> Requires an agent level authentication. Returns a list of CertEnrollmentResult objects.</p>
<dt><code>get_cert(inst, *args, **kwargs)</code></p>
<dd> Return a CertData object for a particular certificate.</p>
<dt><code>get_enrollment_template(inst, *args, **kwargs)</code></p>
<dd> Fetch the enrollment template for the given profile id. For the first time, the request is sent to the server. The retrieved CertEnrollmentRequest object is then cached locally for future requests. Returns a CerEnrollmentRequest object.</p>
<dt><code>get_request(inst, *args, **kwargs)</code></p>
<dd> Get information of a certificate request with the given request ID. Returns a CertRequestInfo object.</p>
<dt><code>hold_cert(inst, *args, **kwargs)</code></p>
<dd> Places a certificate on-hold. Calls the revoke_cert method with reason &#8211; CertRevokeRequest.REASON_CERTIFICATE_HOLD. Returns a CertRequestInfo object. This method requires an agent&#8217;s authentication cert in the connection object.</p>
<dt><code>list_certs(inst, *args, **kwargs)</code></p>
<dd> Return a CertDataInfoCollection object with a information about all the certificates that satisfy the search criteria. If cert_search_request=None, returns all the certificates.</p>
<dt><code>list_enrollment_templates(inst, *args, **kwargs)</code></p>
<dd> Gets the list of profile templates supported by the CA. The values for start and size arguments determine the starting point and the length of the list. Returns a ProfileDataInfoCollection object.</p>
<dt><code>list_requests(inst, *args, **kwargs)</code></p>
<dd> Query for a list of certificates using the arguments passed. Returns a CertRequestInfoCollection object.</p>
<dt><code>reject_request(request_id, cert_review_response=None)</code></p>
<dd> Rejects a certificate enrollment request. If cert_review_response is None, a review request operation is performed to fetch the CertReviewResponse object. Requires as agent level authentication.</p>
<dt><code>review_cert(inst, *args, **kwargs)</code></p>
<dd> Reviews a certificate. Returns a CertData object with a nonce. This method requires an agent&#8217;s authentication cert in the connection object.</p>
<dt><code>review_request(inst, *args, **kwargs)</code></p>
<dd> Reviews a certificate enrollment request. Returns a CertReviewResponse object which contains the nonce from the server needed to perform an action on the request.</p>
<dt><code>revoke_ca_cert(inst, *args, **kwargs)</code></p>
<dd> Revokes a CA certificate. Returns a CertRequestInfo object with information about the request. This method requires an agent&#8217;s authentication cert in the connection object.</p>
<dt><code>revoke_cert(inst, *args, **kwargs)</code></p>
<dd> Revokes a certificate. Returns a CertRequestInfo object with information about the request. This method requires an agent&#8217;s authentication cert in the connection object.</p>
<dt><code>submit_enrollment_request(inst, *args, **kwargs)</code></p>
<dd> Submits the CertEnrollmentRequest object to the server. Returns a CertRequestInfoCollection object with information about the certificate requests enrolled at the CA.</p>
<dt><code>unassign_request(request_id, cert_review_response)</code></p>
<dd> Un-assigns a certificate enrollment request. If cert_review_response is None, a review request operation is performed to fetch the CertReviewResponse object. Requires as agent level authentication.</p>
<dt><code>unrevoke_cert(inst, *args, **kwargs)</code></p>
<dd> Un-revokes a revoked certificate. Returns a CertRequestInfo object. This method requires an agent&#8217;s authentication cert in the connection object.</p>
<dt><code>update_request(request_id, cert_review_response)</code></p>
<dd> Updates a certificate enrollment request. If cert_review_response is None, a review request operation is performed to fetch the CertReviewResponse object. Requires as agent level authentication.</p>
<dt><code>validate_request(request_id, cert_review_response)</code></p>
<dd> Validates a certificate enrollment request. If cert_review_response is None, a review request operation is performed to fetch the CertReviewResponse object. Requires as agent level authentication.</p>
<dt><code>class pki.cert.CertData</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class containing certificate data as returned from getCert()</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd> Return CertData object from JSON dict</p>
<dt><code>json_attribute_names = {&#8216;Nonce&#8217;: &#8216;nonce&#8217;, &#8216;SubjectDN&#8217;: &#8216;subject_dn&#8217;, &#8216;NotBefore&#8217;: &#8216;not_before&#8217;, &#8216;IssuerDN&#8217;: &#8216;issuer_dn&#8217;, &#8216;NotAfter&#8217;: &#8216;not_after&#8217;, &#8216;id&#8217;: &#8216;serial_number&#8217;, &#8216;Status&#8217;: &#8216;status&#8217;, &#8216;PKCS7CertChain&#8217;: &#8216;pkcs7_cert_chain&#8217;, &#8216;PrettyPrint&#8217;: &#8216;pretty_repr&#8217;, &#8216;Link&#8217;: &#8216;link&#8217;, &#8216;Encoded&#8217;: &#8216;encoded&#8217;}</code></p>
<dd>
<dt><code>class pki.cert.CertDataInfo</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class containing information contained in a CertRecord on the CA. This data is returned when searching/listing certificate records.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd> Return CertDataInfo object from JSON dict</p>
<dt><code>json_attribute_names = {&#8216;IssuedOn&#8217;: &#8216;issued_on&#8217;, &#8216;SubjectDN&#8217;: &#8216;subject_dn&#8217;, &#8216;NotValidBefore&#8217;: &#8216;not_valid_before&#8217;, &#8216;Version&#8217;: &#8216;version&#8217;, &#8216;Type&#8217;: &#8216;type&#8217;, &#8216;id&#8217;: &#8216;serial_number&#8217;, &#8216;Status&#8217;: &#8216;status&#8217;, &#8216;NotValidAfter&#8217;: &#8216;not_valid_after&#8217;, &#8216;IssuedBy&#8217;: &#8216;issued_by&#8217;, &#8216;KeyLength&#8217;: &#8216;key_length&#8217;, &#8216;Link&#8217;: &#8216;link&#8217;, &#8216;KeyAlgorithmOID&#8217;: &#8216;key_algorithm_oid&#8217;}</code></p>
<dd>
<dt><code>class pki.cert.CertDataInfoCollection</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class containing list of CertDataInfo objects and their respective link objects. This data is returned when searching/listing certificate records in the CA.</p>
<dt><code>classmethod from_json(json_value)</code></p>
<dd> Populate object from JSON input</p>
<dt><code>class pki.cert.CertEnrollmentRequest(profile_id=None, renewal=False, serial_number=None, remote_host=None, remote_address=None, inputs=None, outputs=None)</code></p>
<dd> Bases: <code>object</code></p>
<dt><code>This class encapsulates the parameters required for a certificate</code></p>
<dd> enrollment request.</p>
<dt><code>add_input(profile_input)</code></p>
<dd>
<dt><code>add_output(profile_output)</code></p>
<dd>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>get_input(profile_input_name)</code></p>
<dd>
<dt><code>get_output(profile_output_name)</code></p>
<dd>
<dt><code>json_attribute_names = {&#8216;RemoteAddress&#8217;: &#8216;remote_address&#8217;, &#8216;RemoteHost&#8217;: &#8216;remote_host&#8217;, &#8216;SerialNumber&#8217;: &#8216;serial_number&#8217;, &#8216;Output&#8217;: &#8216;outputs&#8217;, &#8216;Input&#8217;: &#8216;inputs&#8217;, &#8216;Renewal&#8217;: &#8216;renewal&#8217;, &#8216;ProfileID&#8217;: &#8216;profile_id&#8217;}</code></p>
<dd>
<dt><code>remove_input(profile_input_name)</code></p>
<dd>
<dt><code>remove_output(profile_output_name)</code></p>
<dd>
<dt><code>class pki.cert.CertEnrollmentResult(request, cert)</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class containing results of an enrollment request. </p>
<p> This structure contains information about the cert request generated and any certificates issued.</p>
<dt><code>class pki.cert.CertRequestInfo</code></p>
<dd> Bases: <code>object</code> </p>
<p> An object of this class stores represents a certificate request.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>json_attribute_names = {&#8216;certRequestType&#8217;: &#8216;cert_request_type&#8217;, &#8216;certId&#8217;: &#8216;cert_id&#8217;, &#8216;operationResult&#8217;: &#8216;operation_result&#8217;, &#8216;requestType&#8217;: &#8216;request_type&#8217;, &#8216;requestStatus&#8217;: &#8216;request_status&#8217;, &#8216;errorMessage&#8217;: &#8216;error_message&#8217;, &#8216;requestURL&#8217;: &#8216;request_url&#8217;, &#8216;certURL&#8217;: &#8216;cert_url&#8217;}</code></p>
<dd>
<dt><code>class pki.cert.CertRequestInfoCollection</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class containing list of CertRequestInfo objects. This data is returned when listing certificate request records in the CA.</p>
<dt><code>classmethod from_json(json_value)</code></p>
<dd> Populate object from JSON input</p>
<dt><code>class pki.cert.CertRequestStatus</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class containing valid cert statuses.</p>
<dt><code>CANCELED = &#8216;canceled&#8217;</code></p>
<dd>
<dt><code>COMPLETE = &#8216;complete&#8217;</code></p>
<dd>
<dt><code>PENDING = &#8216;pending&#8217;</code></p>
<dd>
<dt><code>REJECTED = &#8216;rejected&#8217;</code></p>
<dd>
<dt><code>class pki.cert.CertReviewResponse(profile_id=None, renewal=False, serial_number=None, remote_host=None, remote_address=None, inputs=None, outputs=None, nonce=None, request_id=None, request_type=None, request_status=None, request_owner=None, request_creation_time=None, request_modification_time=None, request_notes=None, profile_approval_by=None, profile_set_id=None, profile_is_visible=None, profile_name=None, profile_description=None, profile_remote_host=None, profile_remote_address=None, policy_sets=None)</code></p>
<dd> Bases: <code>pki.cert.CertEnrollmentRequest</code> </p>
<p> An object of this class represent the response from the server when reviewing a certificate enrollment request. It contains a nonce required to perform action on the request.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>json_attribute_names = {&#8216;ProfilePolicySet&#8217;: &#8216;policy_sets&#8217;, &#8216;profileSetId&#8217;: &#8216;profile_set_id&#8217;, &#8216;RemoteAddress&#8217;: &#8216;remote_address&#8217;, &#8216;requestType&#8217;: &#8216;request_type&#8217;, &#8216;RemoteHost&#8217;: &#8216;remote_host&#8217;, &#8216;SerialNumber&#8217;: &#8216;serial_number&#8217;, &#8216;requestCreationTime&#8217;: &#8216;request_creation_time&#8217;, &#8216;requestOwner&#8217;: &#8216;request_owner&#8217;, &#8216;Input&#8217;: &#8216;inputs&#8217;, &#8216;Output&#8217;: &#8216;outputs&#8217;, &#8216;profileIsVisible&#8217;: &#8216;profile_is_visible&#8217;, &#8216;requestStatus&#8217;: &#8216;request_status&#8217;, &#8216;profileRemoteHost&#8217;: &#8216;profile_remote_host&#8217;, &#8216;profileApprovedBy&#8217;: &#8216;profile_approved_by&#8217;, &#8216;requestNotes&#8217;: &#8216;request_notes&#8217;, &#8216;Renewal&#8217;: &#8216;renewal&#8217;, &#8216;profileDescription&#8217;: &#8216;profile_description&#8217;, &#8216;profileRemoteAddr&#8217;: &#8216;profile_remote_address&#8217;, &#8216;ProfileID&#8217;: &#8216;profile_id&#8217;, &#8216;profileName&#8217;: &#8216;profile_name&#8217;, &#8216;requestModificationTime&#8217;: &#8216;request_modification_time&#8217;, &#8216;requestId&#8217;: &#8216;request_id&#8217;}</code></p>
<dd>
<dt><code>class pki.cert.CertRevokeRequest(nonce, reason=None, invalidity_date=None, comments=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> An object of this class encapsulates all the parameters required for revoking a certificate.</p>
<dt><code>Valid values for reasons for revoking a request are:</code></p>
<dd> &#8216;Unspecified&#8217;, &#8216;Key_Compromise&#8217;, &#8216;CA_Compromise&#8217;, &#8216;Affiliation_Changed&#8217;, &#8216;Superseded&#8217;, &#8216;Cessation_of_Operation&#8217;, &#8216;Certificate_Hold&#8217;, &#8216;Remove_from_CRL&#8217;, &#8216;Privilege_Withdrawn&#8217;, &#8216;AA_Compromise&#8217;</p>
<dt><code>reasons = [&#8216;Unspecified&#8217;, &#8216;Key_Compromise&#8217;, &#8216;CA_Compromise&#8217;, &#8216;Affiliation_Changed&#8217;, &#8216;Superseded&#8217;, &#8216;Cessation_of_Operation&#8217;, &#8216;Certificate_Hold&#8217;, &#8216;Remove_from_CRL&#8217;, &#8216;Privilege_Withdrawn&#8217;, &#8216;AA_Compromise&#8217;]</code></p>
<dd>
<dt><code>class pki.cert.CertSearchRequest(**cert_search_params)</code></p>
<dd> Bases: <code>object</code> </p>
<p> An object of this class is used to store the search parameters and send them to server.</p>
<dt><code>search_params = {&#8216;valid_not_before_from&#8217;: &#8216;validNotBeforeFrom&#8217;, &#8216;cert_type_ssl_client&#8217;: &#8216;certTypeSSLClient&#8217;, &#8216;common_name&#8217;: &#8216;commonName&#8217;, &#8216;serial_to&#8217;: &#8216;serialTo&#8217;, &#8216;validity_unit&#8217;: &#8216;validityUnit&#8217;, &#8216;cert_type_sub_ssl_ca&#8217;: &#8216;certTypeSubSSLCA&#8217;, &#8216;user_id&#8217;: &#8216;userID&#8217;, &#8216;locality&#8217;: &#8216;locality&#8217;, &#8216;org_unit&#8217;: &#8216;orgUnit&#8217;, &#8216;issued_by&#8217;: &#8216;issuedBy&#8217;, &#8216;revocation_reason&#8217;: &#8216;revocationReason&#8217;, &#8216;state&#8217;: &#8216;state&#8217;, &#8216;validity_operation&#8217;: &#8216;validityOperation&#8217;, &#8217;email&#8217;: &#8216;eMail&#8217;, &#8216;status&#8217;: &#8216;status&#8217;, &#8216;valid_not_after_from&#8217;: &#8216;validNotAfterFrom&#8217;, &#8216;match_exactly&#8217;: &#8216;matchExactly&#8217;, &#8216;valid_not_before_to&#8217;: &#8216;validNotBeforeTo&#8217;, &#8216;revoked_on_from&#8217;: &#8216;revokedOnFrom&#8217;, &#8216;validity_count&#8217;: &#8216;validityCount&#8217;, &#8216;org&#8217;: &#8216;org&#8217;, &#8216;cert_type_ssl_server&#8217;: &#8216;certTypeSSLServer&#8217;, &#8216;issued_on_from&#8217;: &#8216;issuedOnFrom&#8217;, &#8216;cert_type_sub_email_ca&#8217;: &#8216;certTypeSubEmailCA&#8217;, &#8216;serial_from&#8217;: &#8216;serialFrom&#8217;, &#8216;country&#8217;: &#8216;country&#8217;, &#8216;issued_on_to&#8217;: &#8216;issuedOnTo&#8217;, &#8216;revoked_by&#8217;: &#8216;revokedBy&#8217;, &#8216;valid_not_after_to&#8217;: &#8216;validNotAfterTo&#8217;, &#8216;cert_type_secure_email&#8217;: &#8216;certTypeSecureEmail&#8217;, &#8216;revoked_on_to&#8217;: &#8216;revokedOnTo&#8217;}</code></p>
<dd>
<dt><code>pki.cert.main()</code></p>
<dd></dl>
<h3><code>client</code> Module</h3>
<dl>
<dt><code>class pki.client.PKIConnection(protocol=&#8217;http&#8217;, hostname=&#8217;localhost&#8217;, port=&#8217;8080&#8242;, subsystem=&#8217;ca&#8217;, accept=&#8217;application/json&#8217;, trust_env=None)</code></p>
<dd> Class to encapsulate the connection between the client and a Dogtag subsystem.</p>
<dt><code>authenticate(username=None, password=None)</code></p>
<dd> Set the parameters used for authentication if username/password is to be used. Both username and password must not be None. Note that this method only sets the parameters. Actual authentication occurs when the connection is attempted,</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>username</code> &#8212; username to authenticate connection</p>
<dt>&bull;</p>
<dd> <code>password</code> &#8212; password to authenticate connection</p>
<dt><code>Returns</code></p>
<dd> None</p>
<dt><code>delete(*args, **kwargs)</code></p>
<dd> Uses python-requests to issue a DEL request to the server.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>path</code> (<i>str</i>) &#8212; path URI for the DEL request</p>
<dt>&bull;</p>
<dd> <code>headers</code> (<i>dict</i>) &#8212; headers for the DEL request</p>
<dt><code>Returns</code></p>
<dd> request.response &#8212; response from the server</p>
<dt><code>Raises </code></p>
<dd> Exception from python-requests in case the DEL was not successful, or returns an error code.</p>
<dt><code>get(*args, **kwargs)</code></p>
<dd> Uses python-requests to issue a GET request to the server.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>path</code> (<i>str</i>) &#8212; path URI for the GET request</p>
<dt>&bull;</p>
<dd> <code>headers</code> (<i>dict</i>) &#8212; headers for the GET request</p>
<dt>&bull;</p>
<dd> <code>params</code> (<i>dict or bytes</i>) &#8212; Query parameters for the GET request</p>
<dt>&bull;</p>
<dd> <code>payload</code> (<i>dict, bytes, file-like object</i>) &#8212; data to be sent in the body of the request</p>
<dt><code>Returns</code></p>
<dd> request.response &#8212; response from the server</p>
<dt><code>Raises </code></p>
<dd> Exception from python-requests in case the GET was not successful, or returns an error code.</p>
<dt><code>post(*args, **kwargs)</code></p>
<dd> Uses python-requests to issue a POST request to the server.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>path</code> (<i>str</i>) &#8212; path URI for the POST request</p>
<dt>&bull;</p>
<dd> <code>payload</code> (<i>dict, bytes, file-like object</i>) &#8212; data to be sent in the body of the request</p>
<dt>&bull;</p>
<dd> <code>headers</code> (<i>dict</i>) &#8212; headers for the POST request</p>
<dt>&bull;</p>
<dd> <code>params</code> (<i>dict or bytes</i>) &#8212; Query parameters for the POST request</p>
<dt><code>Returns</code></p>
<dd> request.response &#8212; response from the server</p>
<dt><code>Raises </code></p>
<dd> Exception from python-requests in case the POST was not successful, or returns an error code.</p>
<dt><code>put(*args, **kwargs)</code></p>
<dd> Uses python-requests to issue a PUT request to the server.</p>
<dt><code>Parameters</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>path</code> (<i>str</i>) &#8212; path URI for the PUT request</p>
<dt>&bull;</p>
<dd> <code>payload</code> (<i>dict, bytes, file-like object</i>) &#8212; data to be sent in the body of the request</p>
<dt>&bull;</p>
<dd> <code>headers</code> (<i>dict</i>) &#8212; headers for the PUT request</p>
<dt><code>Returns</code></p>
<dd> request.response &#8212; response from the server</p>
<dt><code>Raises </code></p>
<dd> Exception from python-requests in case the PUT was not successful, or returns an error code.</p>
<dt><code>set_authentication_cert(pem_cert_path)</code></p>
<dd> Set the path to the PEM file containing the certificate and private key for the client certificate to be used for authentication to the server, when client certificate authentication is required.</p>
<dt><code>Parameters</code></p>
<dd> <code>pem_cert_path</code> (<i>str</i>) &#8212; path to the PEM file</p>
<dt><code>Returns</code></p>
<dd> None</p>
<dt><code>Raises </code></p>
<dd> Exception if path is empty or None.</p>
<dt><code>pki.client.catch_insecure_warning(func)</code></p>
<dd> Temporary silence InsecureRequestWarning </p>
<p> PKIConnection is not able to verify HTTPS connections yet. This decorator catches the warning.</p>
<dt><code>See </code></p>
<dd> <i><a rel="nofollow" href="https://fedorahosted.org/pki/ticket/1253">https://fedorahosted.org/pki/ticket/1253</a></i></p>
<dt><code>pki.client.main()</code></p>
<dd> Test code for the PKIConnection class. :return: None</dl>
<h3><code>crypto</code> Module</h3>
<p> Module containing crypto classes.</p>
<dl>
<dt><code>class pki.crypto.CryptoProvider</code></p>
<dd> Bases: <code>object</code> </p>
<p> Abstract class containing methods to do cryptographic operations.</p>
<dt><code>asymmetric_wrap(data, wrapping_cert, mechanism=None)</code></p>
<dd> encrypt a symmetric key with the public key of a transport cert. </p>
<p> The mechanism is the type of symmetric key, which defaults to a 56 bit DES3 key.</p>
<dt><code>static generate_nonce_iv(mechanism)</code></p>
<dd> Create a random initialization vector</p>
<dt><code>generate_session_key()</code></p>
<dd> Generate a session key to be used for wrapping data to the DRM This must return a 3DES 168 bit key</p>
<dt><code>generate_symmetric_key(mechanism=None, size=0)</code></p>
<dd> Generate and return a symmetric key</p>
<dt><code>get_cert(cert_nick)</code></p>
<dd> Get the certificate for the specified cert_nick.</p>
<dt><code>initialize()</code></p>
<dd> Initialization code</p>
<dt><code>symmetric_unwrap(data, wrapping_key, mechanism=None, nonce_iv=None)</code></p>
<dd> decrypt data originally encrypted with symmetric key (wrapping key) </p>
<p> We expect the data and nonce_iv values to be base64 encoded. The mechanism is the type of key used to do the wrapping. It defaults to a 56 bit DES3 key.</p>
<dt><code>symmetric_wrap(data, wrapping_key, mechanism=None, nonce_iv=None)</code></p>
<dd> encrypt data using a symmetric key (wrapping key)</p>
<dt><code>class pki.crypto.NSSCryptoProvider(certdb_dir, certdb_password=None, password_file=None)</code></p>
<dd> Bases: <code>pki.crypto.CryptoProvider</code> </p>
<p> Class that defines NSS implementation of CryptoProvider. Requires an NSS database to have been set up and initialized. </p>
<p> Note that all inputs and outputs are unencoded.</p>
<dt><code>asymmetric_wrap(data, wrapping_cert, mechanism=310)</code></p>
<dd> :param data Data to be wrapped :param wrapping_cert Public key to wrap data :param mechanism algorithm of symmetric key to be wrapped </p>
<p> Wrap (encrypt) data using the supplied asymmetric key</p>
<dt><code>static generate_nonce_iv(mechanism=310)</code></p>
<dd> Create a random initialization vector</p>
<dt><code>generate_session_key()</code></p>
<dd> Returns a session key to be used when wrapping secrets for the DRM This will return a 168 bit 3DES key.</p>
<dt><code>generate_symmetric_key(mechanism=310, size=0)</code></p>
<dd> Returns a symmetric key. </p>
<p> Note that for fixed length keys, this length should be 0. If no length is provided, then the function will either use 0 (for fixed length keys) or the maximum available length for that algorithm and the token.</p>
<dt><code>get_cert(cert_nick)</code></p>
<dd> :param cert_nick Nickname for the certificate to be returned </p>
<p> Searches NSS database and returns SecItem object for this certificate.</p>
<dt><code>import_cert(cert_nick, cert, trust=&#8217;, &#8216;)</code></p>
<dd> Import a certificate into the nss database</p>
<dt><code>initialize()</code></p>
<dd> Initialize the nss db. Must be done before any crypto operations</p>
<dt><code>classmethod setup_contexts(mechanism, sym_key, nonce_iv)</code></p>
<dd> Set up contexts to do wrapping/unwrapping by symmetric keys.</p>
<dt><code>static setup_database(db_dir, password=None, over_write=False, password_file=None)</code></p>
<dd> Create an NSS database</p>
<dt><code>symmetric_unwrap(data, wrapping_key, mechanism=310, nonce_iv=None)</code></p>
<dd> :param data Data to be unwrapped :param wrapping_key Symmetric key to unwrap data :param nonce_iv iv data </p>
<p> Unwrap (decrypt) data using the supplied symmetric key</p>
<dt><code>symmetric_wrap(data, wrapping_key, mechanism=310, nonce_iv=None)</code></p>
<dd> :param data Data to be wrapped :param wrapping_key Symmetric key to wrap data </p>
<p> Wrap (encrypt) data using the supplied symmetric key</dl>
<h3><code>encoder</code> Module</h3>
<dl>
<dt><code>pki.encoder.CustomTypeDecoder(dct)</code></p>
<dd>
<dt><code>class pki.encoder.CustomTypeEncoder(skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, encoding=&#8217;utf-8&#8242;, default=None)</code></p>
<dd> Bases: <code>json.encoder.JSONEncoder</code> </p>
<p> A custom JSONEncoder class that knows how to encode core custom objects. </p>
<p> Custom objects are encoded as JSON object literals (ie, dicts) with one key, &#8216;TypeName&#8217; where &#8216;TypeName&#8217; is the actual name of the type to which the object belongs. That single key maps to another object literal which is just the __dict__ of the object encoded. </p>
<p> Reason for ignoring the error: E0202 &#8211; An attribute affected in json.encoder line 157 hide this method reported by pylint: </p>
<p> The error is in json.encoder.JSONEncoder class. There is a default method (which is overridden here) and also a class attribute self.default initialized in the init method of the class. The intention of such usage being that a custom default method object can be passed to init when creating an instance of JSONEncoder, which is then assigned to class&#8217;s default method. (which is valid) But pylint raises an issue due to the usage of same name for a method and an attribute in which case the attribute definition hides the method. The reason and example for the issue: (top rated comment) <i><a rel="nofollow" href="http://stackoverflow.com/questions/12949064/python-what-happens">http://stackoverflow.com/questions/12949064/python-what-happens</a></i>&#8211; when-instance-variable-name-is-same-as-method-name</p>
<dt><code>static attr_name_conversion(attr_dict, object_class)</code></p>
<dd>
<dt><code>default(obj)</code></p>
<dd>
<dt><code>pki.encoder.decode_cert(data)</code></p>
<dd> base64 decode X.509 certificate</p>
<dt><code>Parameters</code></p>
<dd> <code>data</code> (<i>str, bytes</i>) &#8212; data as bytes or ASCII text</p>
<dt><code>Return type</code></p>
<dd> bytes</p>
<dt><code>pki.encoder.encode_cert(data)</code></p>
<dd> base64 encode X.509 certificate </p>
<p> Python 3&#8217;s base64.b64encode() doesn&#8217;t support ASCII text.</p>
<dt><code>Parameters</code></p>
<dd> <code>data</code> (<i>str, bytes</i>) &#8212; data as bytes or ASCII text</p>
<dt><code>Return type</code></p>
<dd> bytes</dl>
<h3><code>key</code> Module</h3>
<p> Module containing the Python client classes for the KeyClient and KeyRequestClient REST API on a DRM</p>
<dl>
<dt><code>class pki.key.AsymKeyGenerationRequest(client_key_id=None, key_size=None, key_algorithm=None, key_usages=None, trans_wrapped_session_key=None, realm=None)</code></p>
<dd> Bases: <code>pki.ResourceMessage</code> </p>
<p> Class representing the data sent to the DRM when generating and archiving asymmetric keys in the DRM.</p>
<dt><code>DECRYPT_USAGE = &#8216;decrypt&#8217;</code></p>
<dd>
<dt><code>DERIVE_USAGE = &#8216;derive&#8217;</code></p>
<dd>
<dt><code>ENCRYPT_USAGE = &#8216;encrypt&#8217;</code></p>
<dd>
<dt><code>SIGN_RECOVER_USAGE = &#8216;sign_recover&#8217;</code></p>
<dd>
<dt><code>SIGN_USAGE = &#8216;sign&#8217;</code></p>
<dd>
<dt><code>UNWRAP_USAGE = &#8216;unwrap&#8217;</code></p>
<dd>
<dt><code>VERIFY_RECOVER_USAGE = &#8216;verify_recover&#8217;</code></p>
<dd>
<dt><code>VERIFY_USAGE = &#8216;verify&#8217;</code></p>
<dd>
<dt><code>WRAP_USAGE = &#8216;wrap&#8217;</code></p>
<dd>
<dt><code>class pki.key.Key(key_data)</code></p>
<dd> Bases: <code>object</code> </p>
<p> An instance of this class stores the decoded encrypted secret present in the KeyData object passed in the constructor. All the key retrieval requests return this object.</p>
<dt><code>class pki.key.KeyArchivalRequest(client_key_id=None, data_type=None, wrapped_private_data=None, trans_wrapped_session_key=None, pki_archive_options=None, algorithm_oid=None, symkey_params=None, key_algorithm=None, key_size=None, realm=None)</code></p>
<dd> Bases: <code>pki.ResourceMessage</code> </p>
<p> Class representing the object sent to the DRM when archiving a secret.</p>
<dt><code>class pki.key.KeyClient(connection, crypto, transport_cert_nick=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class that encapsulates and mirrors the functions in the KeyResource and KeyRequestResource Java classes in the DRM REST API.</p>
<dt><code>AES_ALGORITHM = &#8216;AES&#8217;</code></p>
<dd>
<dt><code>ASYMMETRIC_KEY_TYPE = &#8216;asymmetricKey&#8217;</code></p>
<dd>
<dt><code>DES3_ALGORITHM = &#8216;DES3&#8217;</code></p>
<dd>
<dt><code>DESEDE_ALGORITHM = &#8216;DESede&#8217;</code></p>
<dd>
<dt><code>DES_ALGORITHM = &#8216;DES&#8217;</code></p>
<dd>
<dt><code>DES_EDE3_CBC_OID = &#8216;{1 2 840 113549 3 7}&#8217;</code></p>
<dd>
<dt><code>DSA_ALGORITHM = &#8216;DSA&#8217;</code></p>
<dd>
<dt><code>KEY_STATUS_ACTIVE = &#8216;active&#8217;</code></p>
<dd>
<dt><code>KEY_STATUS_INACTIVE = &#8216;inactive&#8217;</code></p>
<dd>
<dt><code>PASS_PHRASE_TYPE = &#8216;passPhrase&#8217;</code></p>
<dd>
<dt><code>RC2_ALGORITHM = &#8216;RC2&#8217;</code></p>
<dd>
<dt><code>RC4_ALGORITHM = &#8216;RC4&#8217;</code></p>
<dd>
<dt><code>RSA_ALGORITHM = &#8216;RSA&#8217;</code></p>
<dd>
<dt><code>SYMMETRIC_KEY_TYPE = &#8216;symmetricKey&#8217;</code></p>
<dd>
<dt><code>approve_request(inst, *args, **kwargs)</code></p>
<dd> Approve a secret recovery request</p>
<dt><code>archive_encrypted_data(inst, *args, **kwargs)</code></p>
<dd> Archive a secret (symmetric key or passphrase) on the DRM. </p>
<p> Refer to archive_key() comments for a description of client_key_id, data_type, key_algorithm and key_size.</p>
<dt><code>The following parameters are also required:</code></p>
<dd>
<dt>&bull;</p>
<dd> encrypted_data &#8211; which is the data encrypted by a session key (168 bit 3DES symmetric key)</p>
<dt>&bull;</p>
<dd> wrapped_session_key &#8211; the above session key wrapped by the DRM transport certificate public key.</p>
<dt>&bull;</p>
<dd> the algorithm_oid string for the symmetric key wrap</p>
<dt>&bull;</p>
<dd> the nonce_iv for the symmetric key wrap </p>
<p> This function is useful if the caller wants to do their own wrapping of the secret, or if the secret was generated on a separate client machine and the wrapping was done there. </p>
<p> The function returns a KeyRequestResponse object containing a KeyRequestInfo object with details about the archival request and key archived.</p>
<dt><code>archive_key(inst, *args, **kwargs)</code></p>
<dd> Archive a secret (symmetric key or passphrase) on the DRM. </p>
<p> Requires a user-supplied client ID. There can be only one active key with a specified client ID. If a record for a duplicate active key exists, a BadRequestException is thrown.</p>
<dt><code>data_type can be one of the following:</code></p>
<dd> KeyClient.SYMMETRIC_KEY_TYPE, KeyClient.ASYMMETRIC_KEY_TYPE, KeyClient.PASS_PHRASE_TYPE </p>
<p> key_algorithm and key_size are applicable to symmetric keys only. If a symmetric key is being archived, these parameters are required. </p>
<p> private_data is the raw secret to be archived. It will be wrapped and sent to the DRM. </p>
<p> The function returns a KeyRequestResponse object containing a KeyRequestInfo object with details about the archival request and key archived.</p>
<dt><code>archive_pki_options(inst, *args, **kwargs)</code></p>
<dd> Archive a secret (symmetric key or passphrase) on the DRM. </p>
<p> Refer to archive_key() comments for a description of client_key_id, data_type, key_algorithm and key_size. </p>
<p> pki_archive_options is the data to be archived wrapped in a PKIArchiveOptions structure, </p>
<p> The function returns a KeyRequestResponse object containing a KeyRequestInfo object with details about the archival request and key archived.</p>
<dt><code>cancel_request(inst, *args, **kwargs)</code></p>
<dd> Cancel a secret recovery request</p>
<dt><code>generate_asymmetric_key(inst, *args, **kwargs)</code></p>
<dd> Generate and archive asymmetric keys in the DRM. Supports algorithms RSA and DSA. Valid key size for RSA = 256 + (16 * n), where n: 0-496 Valid key size for DSA = 512, 768, 1024. p,q,g params are not supported. </p>
<p> Return a KeyRequestResponse which contains a KeyRequestInfo object that describes the URL for the request and generated keys.</p>
<dt><code>generate_symmetric_key(inst, *args, **kwargs)</code></p>
<dd> Generate and archive a symmetric key on the DRM. </p>
<p> Return a KeyRequestResponse which contains a KeyRequestInfo object that describes the URL for the request and generated key.</p>
<dt><code>get_active_key_info(inst, *args, **kwargs)</code></p>
<dd> Get the info in the KeyRecord for the active secret in the DRM.</p>
<dt><code>get_key_info(inst, *args, **kwargs)</code></p>
<dd> Get the info in the KeyRecord for a specific secret in the DRM.</p>
<dt><code>get_request_info(inst, *args, **kwargs)</code></p>
<dd> Return a KeyRequestInfo object for a specific request.</p>
<dt><code>list_keys(inst, *args, **kwargs)</code></p>
<dd> List/Search archived secrets in the DRM. </p>
<p> See KRAClient.list_keys for the valid values of status. Returns a KeyInfoCollection object.</p>
<dt><code>list_requests(inst, *args, **kwargs)</code></p>
<dd> List/Search key requests in the DRM. </p>
<p> See KRAClient.list_requests for the valid values of request_state and request_type. Returns a KeyRequestInfoCollection object.</p>
<dt><code>modify_key_status(inst, *args, **kwargs)</code></p>
<dd> Modify the status of a key</p>
<dt><code>recover_key(inst, *args, **kwargs)</code></p>
<dd> Create a request to recover a secret. </p>
<p> To retrieve a symmetric key or passphrase, the only parameter that is required is the keyId. It is possible (but not required) to pass in the session keys/passphrase and nonceData for the retrieval at this time. Those parameters are documented in the docstring for retrieve_key below. </p>
<p> To retrieve an asymmetric key, the keyId and the the base-64 encoded certificate is required.</p>
<dt><code>reject_request(inst, *args, **kwargs)</code></p>
<dd> Reject a secret recovery request.</p>
<dt><code>retrieve_key(inst, *args, **kwargs)</code></p>
<dd> Retrieve a secret (passphrase or symmetric key) from the DRM. </p>
<p> This function generates a key recovery request, approves it, and retrieves the secret referred to by key_id. This assumes that only one approval is required to authorize the recovery. </p>
<p> To ensure data security in transit, the data will be returned encrypted by a session key (168 bit 3DES symmetric key) &#8211; which is first wrapped (encrypted) by the public key of the DRM transport certificate before being sent to the DRM. The parameter trans_wrapped_session_key refers to this wrapped session key. </p>
<p> There are two ways of using this function:</p>
<dt>1.</p>
<dd> trans_wrapped_session_key is not provided by caller. </p>
<p> In this case, the function will call CryptoProvider methods to generate and wrap the session key. The function will return the KeyData object with a private_data attribute which stores the unwrapped key information.</p>
<dt>2.</p>
<dd> The trans_wrapped_session_key is provided by the caller. </p>
<p> In this case, the function will simply pass the data to the DRM, and will return the secret wrapped in the session key. The secret will still need to be unwrapped by the caller. </p>
<p> The function will return the KeyData object, where the KeyData structure includes the wrapped secret and some nonce data to be used as a salt when unwrapping.</p>
<dt><code>retrieve_key_by_passphrase(inst, *args, **kwargs)</code></p>
<dd> Retrieve a secret (passphrase or symmetric key) from the DRM using a passphrase. </p>
<p> This function generates a key recovery request, approves it, and retrieves the secret referred to by key_id. This assumes that only one approval is required to authorize the recovery. </p>
<p> The secret is secured in transit by wrapping the secret with a passphrase using PBE encryption. </p>
<p> There are two ways of using this function:</p>
<dt>1.</p>
<dd> A passphrase is provided by the caller. </p>
<p> In this case, CryptoProvider methods will be called to create the data to securely send the passphrase to the DRM. Basically, three pieces of data will be sent:</p>
<dt>&bull;</p>
<dd> the passphrase wrapped by a 168 bit 3DES symmetric key (the session key). This is referred to as the parameter session_wrapped_passphrase.</p>
<dt>&bull;</p>
<dd> the session key wrapped with the public key in the DRM transport certificate. This is referred to as the trans_wrapped_session_key.</p>
<dt>&bull;</p>
<dd> ivps nonce data, referred to as nonce_data </p>
<p> The function will return the tuple (KeyData, unwrapped_secret)</p>
<dt>2.</p>
<dd> The caller provides the trans_wrapped_session_key, session_wrapped_passphrase and nonce_data. </p>
<p> In this case, the data will simply be passed to the DRM. The function will return the secret encrypted by the passphrase using PBE Encryption. The secret will still need to be decrypted by the caller. </p>
<p> The function will return the tuple (KeyData, None)</p>
<dt><code>retrieve_key_by_pkcs12(inst, *args, **kwargs)</code></p>
<dd> Retrieve an asymmetric private key and return it as PKCS12 data. </p>
<p> This function generates a key recovery request, approves it, and retrieves the secret referred to by key_id in a PKCS12 file. This assumes that only one approval is required to authorize the recovery. </p>
<p> This function requires the following parameters: &#8211; key_id : the ID of the key &#8211; certificate: the certificate associated with the private key &#8211; passphrase: A passphrase for the pkcs12 file. </p>
<p> The function returns a KeyData object.</p>
<dt><code>retrieve_key_data(inst, *args, **kwargs)</code></p>
<dd> Retrieve a secret from the DRM. </p>
<p> @param: data &#8211; a KeyRecoveryRequest containing the keyId of the secret being retrieved, the request_id of the approved recovery request and a wrapping mechanism. More details at KRAClient.retrieve_key. </p>
<p> Returns a KeyData object containing the wrapped secret.</p>
<dt><code>set_transport_cert(transport_cert_nick)</code></p>
<dd> Set the transport certificate for crypto operations</p>
<dt><code>submit_request(inst, *args, **kwargs)</code></p>
<dd> Submit an archival, recovery or key generation request to the DRM. </p>
<p> @param request &#8211; is either a KeyArchivalRequest, KeyRecoverRequest, SymKeyGenerationRequest or AsymKeyGenerationRequest. </p>
<p> returns a KeyRequestResponse object.</p>
<dt><code>class pki.key.KeyData</code></p>
<dd> Bases: <code>object</code> </p>
<p> This is the object that contains the encoded wrapped secret when that secret is retrieved. It is used by the DRM to send information of the key in the key retrieval requests.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd> Return a KeyData object from a JSON dict</p>
<dt><code>json_attribute_names = {&#8216;nonceData&#8217;: &#8216;nonce_data&#8217;, &#8216;wrappedPrivateData&#8217;: &#8216;wrapped_private_data&#8217;}</code></p>
<dd>
<dt><code>class pki.key.KeyInfo</code></p>
<dd> Bases: <code>object</code> </p>
<p> This is the object that contains information stored in the database record for an archived secret. It does not contain the secret itself.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd> Return KeyInfo from JSON dict</p>
<dt><code>get_key_id()</code></p>
<dd> Return the key ID as parsed from key URL</p>
<dt><code>json_attribute_names = {&#8216;publicKey&#8217;: &#8216;public_key&#8217;, &#8216;clientKeyID&#8217;: &#8216;client_key_id&#8217;, &#8216;ownerName&#8217;: &#8216;owner_name&#8217;, &#8216;keyURL&#8217;: &#8216;key_url&#8217;}</code></p>
<dd>
<dt><code>class pki.key.KeyInfoCollection</code></p>
<dd> Bases: <code>object</code> </p>
<p> This class represents data returned when searching the DRM archived secrets. Essentially, its a list of KeyInfo objects.</p>
<dt><code>classmethod from_json(json_value)</code></p>
<dd> Return a KeyInfoCollection object from its JSON representation</p>
<dt><code>class pki.key.KeyRecoveryRequest(key_id=None, request_id=None, trans_wrapped_session_key=None, session_wrapped_passphrase=None, nonce_data=None, certificate=None, passphrase=None)</code></p>
<dd> Bases: <code>pki.ResourceMessage</code> </p>
<p> Class representing the data sent to the DRM when either creating a request for the recovery of a secret, or, once the request is approved, retrieving the secret.</p>
<dt><code>class pki.key.KeyRequestInfo</code></p>
<dd> Bases: <code>object</code> </p>
<p> This class represents data about key requests (archival, recovery, key generation etc.) in the DRM.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd> Return a KeyRequestInfo object from a JSON dict.</p>
<dt><code>get_key_id()</code></p>
<dd> Return the ID of the secret referred to by this request.</p>
<dt><code>get_request_id()</code></p>
<dd> Return the request ID by parsing the request URL.</p>
<dt><code>json_attribute_names = {&#8216;requestType&#8217;: &#8216;request_type&#8217;, &#8216;requestStatus&#8217;: &#8216;request_status&#8217;, &#8216;requestURL&#8217;: &#8216;request_url&#8217;, &#8216;keyURL&#8217;: &#8216;key_url&#8217;}</code></p>
<dd>
<dt><code>class pki.key.KeyRequestInfoCollection</code></p>
<dd> Bases: <code>object</code> </p>
<p> This class represents the data returned when searching the key requests in the DRM. Essentially, its a list of KeyRequestInfo objects.</p>
<dt><code>classmethod from_json(json_value)</code></p>
<dd> Return a KeyRequestInfoCollection object from its JSON representation.</p>
<dt><code>class pki.key.KeyRequestResponse</code></p>
<dd> Bases: <code>object</code> </p>
<p> This class is returned when an archival, recovery or key generation request is created. It includes a KeyRequestInfo object with information about the created request, and a KeyData structure which contains the wrapped secret (if that operation is supported).</p>
<dt><code>classmethod from_json(json_value)</code></p>
<dd> Return a KeyRequestResponse object from its JSON representation.</p>
<dt><code>get_key_id()</code></p>
<dd> Return the id for the key archived, recovered or generated</p>
<dt><code>get_request_id()</code></p>
<dd> Return the id for the created request</p>
<dt><code>class pki.key.RequestId(req_id)</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class representing a Request ID</p>
<dt><code>class pki.key.SymKeyGenerationRequest(client_key_id=None, key_size=None, key_algorithm=None, key_usages=None, trans_wrapped_session_key=None, realm=None)</code></p>
<dd> Bases: <code>pki.ResourceMessage</code> </p>
<p> Class representing the data sent to the DRM when generating and archiving a symmetric key in the DRM.</p>
<dt><code>DECRYPT_USAGE = &#8216;decrypt&#8217;</code></p>
<dd>
<dt><code>ENCRYPT_USAGE = &#8216;encrypt&#8217;</code></p>
<dd>
<dt><code>SIGN_USAGE = &#8216;sign&#8217;</code></p>
<dd>
<dt><code>UNWRAP_USAGE = &#8216;unwrap&#8217;</code></p>
<dd>
<dt><code>VERIFY_USAGE = &#8216;verify&#8217;</code></p>
<dd>
<dt><code>WRAP_USAGE = &#8216;wrap&#8217;</code></p>
<dd>
<dt><code>pki.key.main()</code></p>
<dd> Some unit tests &#8211; basically printing different types of requests</dl>
<h3><code>kra</code> Module</h3>
<p> Module containing KRAClient class. This class should be used by Python clients to interact with the DRM to expose the functionality of the KeyClient and KeyRequestResource REST APIs.</p>
<dl>
<dt><code>class pki.kra.KRAClient(connection, crypto, transport_cert_nick=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> Client class that models interactions with a KRA using the Key and KeyRequest REST APIs.</dl>
<h3><code>profile</code> Module</h3>
<dl>
<dt><code>class pki.profile.Descriptor(syntax=None, constraint=None, description=None, default_value=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> This class represents the description of a ProfileAttribute. It stores information such as the syntax, constraint and default value of a profile attribute.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>json_attribute_names = {&#8216;DefaultValue&#8217;: &#8216;default_value&#8217;, &#8216;Constraint&#8217;: &#8216;constraint&#8217;, &#8216;Description&#8217;: &#8216;description&#8217;, &#8216;Syntax&#8217;: &#8216;syntax&#8217;}</code></p>
<dd>
<dt><code>class pki.profile.PolicyConstraint(name=None, description=None, class_id=None, policy_constraint_values=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> An object of this class contains the policy constraints applied to a ProfileInput used by a certificate enrollment request.</p>
<dt><code>add_constraint_value(policy_constraint_value)</code></p>
<dd> Add a PolicyConstraintValue to the policy_constraint_values list.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>get_constraint_value(policy_constraint_value_name)</code></p>
<dd> Returns a PolicyConstraintValue object with the given name. None, if there is no match.</p>
<dt><code>json_attribute_names = {&#8216;classId&#8217;: &#8216;class_id&#8217;, &#8216;id&#8217;: &#8216;name&#8217;, &#8216;constraint&#8217;: &#8216;policy_constraint_values&#8217;}</code></p>
<dd>
<dt><code>remove_constraint_value(policy_constraint_value_name)</code></p>
<dd> Removes a PolicyConstraintValue with the given name form the policy_constraint_values list.</p>
<dt><code>class pki.profile.PolicyConstraintValue(name=None, value=None, descriptor=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> Represents a PolicyConstraintValue</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>name</code></p>
<dd>
<dt><code>class pki.profile.PolicyDefault(name=None, class_id=None, description=None, policy_attributes=None, policy_params=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> An object of this class contains information of the default usage of a specific ProfileInput.</p>
<dt><code>add_attribute(policy_attribute)</code></p>
<dd> Add a policy attribute to the attribute list. @param policy_attribute &#8211; A ProfileAttribute object</p>
<dt><code>add_parameter(policy_parameter)</code></p>
<dd> Add a profile parameter to the parameters list. @param policy_parameter &#8211; A ProfileParameter object.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>get_attribute(policy_attribute_name)</code></p>
<dd> Fetch the policy attribute with the given name from the attributes list.</p>
<dt><code>get_parameter(profile_parameter_name)</code></p>
<dd> Fetch a profile parameter with the given name from the parameters list.</p>
<dt><code>json_attribute_names = {&#8216;classId&#8217;: &#8216;class_id&#8217;, &#8216;params&#8217;: &#8216;policy_params&#8217;, &#8216;id&#8217;: &#8216;name&#8217;, &#8216;policyAttribute&#8217;: &#8216;policy_attributes&#8217;}</code></p>
<dd>
<dt><code>remove_attribute(policy_attribute_name)</code></p>
<dd> Remove a policy attribute with the given name from the attributes list.</p>
<dt><code>remove_parameter(profile_parameter_name)</code></p>
<dd> Remove a profile parameter with the given name from the parameters list.</p>
<dt><code>class pki.profile.PolicySet(name=None, policy_list=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> An object of this class contains a name value pair of the policy name and the ProfilePolicy object.</p>
<dt><code>add_policy(profile_policy)</code></p>
<dd> Add a ProfilePolicy object to the policy_list</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>get_policy(policy_id)</code></p>
<dd> Returns a ProfilePolicy object with the given profile id.</p>
<dt><code>json_attribute_names = {&#8216;id&#8217;: &#8216;name&#8217;, &#8216;value&#8217;: &#8216;policy_list&#8217;}</code></p>
<dd>
<dt><code>remove_policy(policy_id)</code></p>
<dd> Removes a ProfilePolicy with the given ID from the PolicySet.</p>
<dt><code>class pki.profile.PolicySetList(policy_sets=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> An object of this class stores a list of ProfileSet objects.</p>
<dt><code>add_policy_set(policy_set)</code></p>
<dd> Add a PolicySet object to the policy_sets list.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>get_policy_set(policy_set_name)</code></p>
<dd> Fetch the PolicySet object for the given name. Returns None, if not found.</p>
<dt><code>policy_sets</code></p>
<dd>
<dt><code>remove_policy_set(policy_set_name)</code></p>
<dd> Remove a PolicySet object with the given name from the policy_sets list.</p>
<dt><code>class pki.profile.Profile(profile_id=None, class_id=None, name=None, description=None, enabled=None, visible=None, enabled_by=None, authenticator_id=None, authorization_acl=None, renewal=None, xml_output=None, inputs=None, outputs=None, policy_set_list=None, link=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> This class represents an enrollment profile.</p>
<dt><code>add_input(profile_input)</code></p>
<dd> Add a ProfileInput object to the inputs list of the Profile.</p>
<dt><code>add_output(profile_output)</code></p>
<dd> Add a ProfileOutput object to the outputs list of the Profile.</p>
<dt><code>add_policy_set(policy_set)</code></p>
<dd> Add a PolicySet object to the policy_sets list of the Profile.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>get_input(profile_input_id)</code></p>
<dd> Fetches a ProfileInput with the given ProfileInput id. Returns None, if there is no matching input.</p>
<dt><code>get_output(profile_output_id)</code></p>
<dd> Fetches a ProfileOutput with the given ProfileOutput id. Returns None, if there is no matching output.</p>
<dt><code>get_policy_set(policy_set_name)</code></p>
<dd> Fetches a ProfileInput with the given ProfileInput id. Returns None, if there is no matching input.</p>
<dt><code>static get_profile_data_from_file(path_to_file)</code></p>
<dd> Reads the file for the serialized Profile object. Currently supports only data format in json.</p>
<dt><code>json_attribute_names = {&#8216;classId&#8217;: &#8216;class_id&#8217;, &#8216;authenticatorId&#8217;: &#8216;authenticator_id&#8217;, &#8216;Output&#8217;: &#8216;outputs&#8217;, &#8216;PolicySets&#8217;: &#8216;policy_set_list&#8217;, &#8216;xmlOutput&#8217;: &#8216;xml_output&#8217;, &#8216;authzAcl&#8217;: &#8216;authorization_acl&#8217;, &#8216;enabledBy&#8217;: &#8216;enabled_by&#8217;, &#8216;Input&#8217;: &#8216;inputs&#8217;, &#8216;id&#8217;: &#8216;profile_id&#8217;}</code></p>
<dd>
<dt><code>remove_input(profile_input_id)</code></p>
<dd> Remove a ProfileInput from the inputs list of the Profile.</p>
<dt><code>remove_output(profile_output_id)</code></p>
<dd> Remove a ProfileOutput from the outputs list of the Profile.</p>
<dt><code>remove_policy_set(policy_set_name)</code></p>
<dd> Remove a PolicySet from the policy_sets list of the Profile.</p>
<dt><code>class pki.profile.ProfileAttribute(name=None, value=None, descriptor=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> Represents a profile attribute of a ProfileInput.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>json_attribute_names = {&#8216;Descriptor&#8217;: &#8216;descriptor&#8217;, &#8216;Value&#8217;: &#8216;value&#8217;}</code></p>
<dd>
<dt><code>class pki.profile.ProfileClient(connection)</code></p>
<dd> Bases: <code>object</code> </p>
<p> This class consists of methods for accessing the ProfileResource.</p>
<dt><code>create_profile(inst, *args, **kwargs)</code></p>
<dd> Create a new profile for the given Profile object.</p>
<dt><code>create_profile_from_file(path_to_file)</code></p>
<dd> Reads the file for the serialized Profile object. Performs the profile create operation. Currently supports only data format in json.</p>
<dt><code>delete_profile(inst, *args, **kwargs)</code></p>
<dd> Delete a profile with the given Profile Id.</p>
<dt><code>disable_profile(inst, *args, **kwargs)</code></p>
<dd> Disables a profile.</p>
<dt><code>enable_profile(inst, *args, **kwargs)</code></p>
<dd> Enables a profile.</p>
<dt><code>get_profile(inst, *args, **kwargs)</code></p>
<dd> Fetches information for the profile for the given profile id. Returns a ProfileData object.</p>
<dt><code>list_profiles(inst, *args, **kwargs)</code></p>
<dd> Fetches the list of profiles. The start and size arguments provide pagination support. Returns a ProfileDataInfoCollection object.</p>
<dt><code>modify_profile(inst, *args, **kwargs)</code></p>
<dd> Modify an existing profile with the given Profile object.</p>
<dt><code>modify_profile_from_file(path_to_file)</code></p>
<dd> Reads the file for the serialized Profile object. Performs the profile modify operation. Currently supports only data format in json.</p>
<dt><code>class pki.profile.ProfileDataInfo</code></p>
<dd> Bases: <code>object</code> </p>
<p> Stores information about a profile</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>json_attribute_names = {&#8216;profileDescription&#8217;: &#8216;profile_description&#8217;, &#8216;profileId&#8217;: &#8216;profile_id&#8217;, &#8216;profileURL&#8217;: &#8216;profile_url&#8217;, &#8216;profileName&#8217;: &#8216;profile_name&#8217;}</code></p>
<dd>
<dt><code>class pki.profile.ProfileDataInfoCollection</code></p>
<dd> Bases: <code>object</code> </p>
<p> Represents a collection of ProfileDataInfo objects. Also encapsulates the links for the list of the objects stored.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>class pki.profile.ProfileInput(profile_input_id=None, class_id=None, name=None, text=None, attributes=None, config_attributes=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> This class encapsulates all the attributes of a profile to generate a specific property of a certificate. Ex. Subject name, Requestor Information etc.</p>
<dt><code>add_attribute(profile_attribute)</code></p>
<dd> Add a ProfileAttribute object to the attributes list.</p>
<dt><code>add_config_attribute(profile_attribute)</code></p>
<dd> Add a ProfileAttribute object to the config_attributes list.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>get_attribute(profile_attribute_name)</code></p>
<dd> Returns a ProfileAttribute object for the given name. None, if no match.</p>
<dt><code>get_config_attribute(config_attribute_name)</code></p>
<dd> Returns a ProfileAttribute object with the given name. None, if there is no match in the config_attributes list.</p>
<dt><code>json_attribute_names = {&#8216;ClassID&#8217;: &#8216;class_id&#8217;, &#8216;Name&#8217;: &#8216;name&#8217;, &#8216;Text&#8217;: &#8216;text&#8217;, &#8216;ConfigAttribute&#8217;: &#8216;config_attributes&#8217;, &#8216;Attribute&#8217;: &#8216;attributes&#8217;, &#8216;id&#8217;: &#8216;profile_input_id&#8217;}</code></p>
<dd>
<dt><code>remove_attribute(profile_attribute_name)</code></p>
<dd> Remove a ProfileAttribute object with the given name from the attributes list.</p>
<dt><code>remove_config_attribute(config_attribute_name)</code></p>
<dd> Remove a ProfileAttribute object with the given name from the config_attributes list.</p>
<dt><code>class pki.profile.ProfileOutput(profile_output_id=None, name=None, text=None, class_id=None, attributes=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> This class defines the output of a certificate enrollment request using a profile.</p>
<dt><code>add_attribute(profile_attribute)</code></p>
<dd> Add a ProfileAttribute object to the attributes list.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>get_attribute(profile_attribute_name)</code></p>
<dd> Returns a ProfileAttribute object for the given name. None, if no match.</p>
<dt><code>json_attribute_names = {&#8216;classId&#8217;: &#8216;class_id&#8217;, &#8216;id&#8217;: &#8216;profile_output_id&#8217;}</code></p>
<dd>
<dt><code>remove_attribute(profile_attribute_name)</code></p>
<dd> Remove a ProfileAttribute object with the given name from the attributes list.</p>
<dt><code>class pki.profile.ProfileParameter(name=None, value=None)</code></p>
<dd> Bases: <code>object</code></p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>class pki.profile.ProfilePolicy(policy_id=None, policy_default=None, policy_constraint=None)</code></p>
<dd> Bases: <code>object</code> </p>
<p> This class represents the policy a profile adheres to. An object of this class stores the default values for profile and the constraints present on the values of the attributes of the profile submitted for an enrollment request.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>json_attribute_names = {&#8216;id&#8217;: &#8216;policy_id&#8217;, &#8216;def&#8217;: &#8216;policy_default&#8217;, &#8216;constraint&#8217;: &#8216;policy_constraint&#8217;}</code></p>
<dd>
<dt><code>class pki.profile.ProfilePolicySet</code></p>
<dd> Bases: <code>object</code> </p>
<p> Stores a list of ProfilePolicy objects.</p>
<dt><code>classmethod from_json(attr_list)</code></p>
<dd>
<dt><code>pki.profile.main()</code></p>
<dd></dl>
<h3><code>system</code> Module</h3>
<dl>
<dt><code>class pki.system.ConfigurationRequest</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class used to represent a configuration request to be submitted to the Java installation servlet during the execution of pkispawn. </p>
<p> This class is the python equivalent of the Java class: com.netscape.certsrv.system.ConfigurationRequest</p>
<dt><code>class pki.system.ConfigurationResponse</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class used to represent the response from the Java configuration servlet during the execution of pkispawn. </p>
<p> This class is the python equivalent of the Java class: com.netscape.certsrv.system.ConfigurationRequest</p>
<dt><code>class pki.system.SecurityDomainClient(connection)</code></p>
<dd> Bases: <code>object</code> </p>
<p> Client used to get the security domain from a security domain CA. The connection details for the security domain CA are specified in a PKIConnection object used to construct this client.</p>
<dt><code>get_old_security_domain_info()</code></p>
<dd> Contact the security domain CA specified in the connection object used to construct this client and get the security domain using the old servlet-based interface. This method is useful when contacting old servers which do not provide the REST API.</p>
<dt><code>Returns</code></p>
<dd> pki.system.SecurityDomainInfo</p>
<dt><code>get_security_domain_info()</code></p>
<dd> Contact the security domain CA specified in the connection object used to construct this client and get the security domain using the REST API.</p>
<dt><code>Returns</code></p>
<dd> pki.system.SecurityDomainInfo</p>
<dt><code>class pki.system.SecurityDomainHost</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class representing a security domain host.</p>
<dt><code>classmethod from_json(json_value)</code></p>
<dd> Constructs a SecurityDomainHost object from JSON.</p>
<dt><code>Parameters</code></p>
<dd> <code>json_value</code> (<i>str</i>) &#8212; JSON string representing a security domain host.</p>
<dt><code>Returns</code></p>
<dd> SecurityDomainHost</p>
<dt><code>class pki.system.SecurityDomainInfo</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class representing the entire security domain. This is essentially a list of SecurityDomainSubsystem components.</p>
<dt><code>classmethod from_json(json_value)</code></p>
<dd> Create a SecurityDomainInfo object from JSON.</p>
<dt><code>Parameters</code></p>
<dd> <code>json_value</code> (<i>str</i>) &#8212; JSON representation of a security domain.</p>
<dt><code>Returns</code></p>
<dd> SecurityDomainInfo</p>
<dt><code>class pki.system.SecurityDomainSubsystem</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class representing a security domain subsystem. This is essentially a list of SecurityDomainHost objects of a particular subsystem type (ca, kra, tps, tks, ocsp).</p>
<dt><code>classmethod from_json(json_value)</code></p>
<dd> Constructs a SecurityDomainSubsystem from a JSON representation.</p>
<dt><code>Parameters</code></p>
<dd> <code>json_value</code> (<i>str</i>) &#8212; JSON representation of the Security Domain Subsystem</p>
<dt><code>Returns</code></p>
<dd> SecurityDomainSubsystem</p>
<dt><code>class pki.system.SystemCertData</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class used to represent the data for a system certificate, which is used in the data passed into and returned from the Java installation servlet during the execution of pkispawn. </p>
<p> This class is the python equivalent of the Java class: com.netscape.certsrv.system.SystemCertData</p>
<dt><code>class pki.system.SystemConfigClient(connection)</code></p>
<dd> Bases: <code>object</code> </p>
<p> Client used to interact with the Java configuration servlet to configure a Dogtag subsystem during the execution of pkispawn. </p>
<p> The connection details for the system being configured are passed in the PKIConnection object used when constructing this object.</p>
<dt><code>configure(data)</code></p>
<dd> Contacts the server and invokes the Java configuration REST API to configure a Dogtag subsystem.</p>
<dt><code>Parameters</code></p>
<dd> <code>data</code> (<i>ConfigurationRequest</i>) &#8212; Configuration request containing all the input needed to configure the subsystem</p>
<dt><code>Returns</code></p>
<dd> ConfigurationResponse &#8212; response from configuration servlet.</p>
<dt><code>class pki.system.SystemStatusClient(connection)</code></p>
<dd> Bases: <code>object</code> </p>
<p> Client used to check the status of a Dogtag subsystem.</p>
<dt><code>get_status()</code></p>
<dd> Checks the status of the subsystem by calling the getStatus() servlet. This is used to determine if the server is up and ready to receive and process requests.</p>
<dt><code>Returns</code></p>
<dd> str &#8211; getStatus response</dl>
<h3><code>systemcert</code> Module</h3>
<p> Module containing the Python client classes for the SystemCert REST API</p>
<dl>
<dt><code>class pki.systemcert.SystemCertClient(connection)</code></p>
<dd> Bases: <code>object</code> </p>
<p> Class encapsulating and mirroring the functionality in the SystemCertResource Java interface class defining the REST API for system certificate resources.</p>
<dt><code>get_transport_cert(inst, *args, **kwargs)</code></p>
<dd> Return transport certificate.</p>
<dt><code>Returns</code></p>
<dd> pki.cert.CertData &#8212; transport certificate data</dl>
<h3><code>upgrade</code> Module</h3>
<dl>
<dt><code>class pki.upgrade.PKIUpgradeScriptlet</code></p>
<dd> Bases: <code>object</code></p>
<dt><code>backup(path)</code></p>
<dd>
<dt><code>can_upgrade()</code></p>
<dd>
<dt><code>get_backup_dir()</code></p>
<dd>
<dt><code>init()</code></p>
<dd>
<dt><code>revert()</code></p>
<dd>
<dt><code>update_tracker()</code></p>
<dd>
<dt><code>upgrade()</code></p>
<dd>
<dt><code>upgrade_system()</code></p>
<dd>
<dt><code>class pki.upgrade.PKIUpgradeTracker(name, filename, delimiter=&#8217;=&#8217;, version_key=&#8217;PKI_VERSION&#8217;, index_key=&#8217;PKI_UPGRADE_INDEX&#8217;)</code></p>
<dd> Bases: <code>object</code></p>
<dt><code>get_index()</code></p>
<dd>
<dt><code>get_version()</code></p>
<dd>
<dt><code>remove()</code></p>
<dd>
<dt><code>remove_index()</code></p>
<dd>
<dt><code>remove_version()</code></p>
<dd>
<dt><code>set(version)</code></p>
<dd>
<dt><code>set_index(index)</code></p>
<dd>
<dt><code>set_version(version)</code></p>
<dd>
<dt><code>show()</code></p>
<dd>
<dt><code>class pki.upgrade.PKIUpgrader(upgrade_dir=&#8217;/usr/share/pki/upgrade&#8217;, version=None, index=None, silent=False)</code></p>
<dd> Bases: <code>object</code></p>
<dt><code>all_versions()</code></p>
<dd>
<dt><code>get_current_version()</code></p>
<dd>
<dt><code>get_target_version()</code></p>
<dd>
<dt><code>get_tracker()</code></p>
<dd>
<dt><code>is_complete()</code></p>
<dd>
<dt><code>remove_tracker()</code></p>
<dd>
<dt><code>reset_tracker()</code></p>
<dd>
<dt><code>revert()</code></p>
<dd>
<dt><code>revert_version(version)</code></p>
<dd>
<dt><code>scriptlets(version)</code></p>
<dd>
<dt><code>set_tracker(version)</code></p>
<dd>
<dt><code>show_tracker()</code></p>
<dd>
<dt><code>status()</code></p>
<dd>
<dt><code>upgrade()</code></p>
<dd>
<dt><code>upgrade_version(version)</code></p>
<dd>
<dt><code>version_dir(version)</code></p>
<dd>
<dt><code>versions()</code></p>
<dd>
<dt><code>class pki.upgrade.Version(obj)</code></p>
<dd> Bases: <code>object</code></dl>
<h3><code>util</code> Module</h3>
<p> Module containing utility functions and classes for the Dogtag python code</p>
<dl>
<dt><code>pki.util.chown(path, uid, gid)</code></p>
<dd> Change ownership of a folder and its contents.</p>
<dt><code>pki.util.copy(source, dest)</code></p>
<dd> Copy a file or a folder and its contents.</p>
<dt><code>pki.util.copydirs(source, dest)</code></p>
<dd> Copy a folder and its parents while preserving their attributes.</p>
<dt><code>pki.util.copyfile(source, dest, overwrite=True)</code></p>
<dd> Copy a file or link while preserving its attributes.</p>
<dt><code>pki.util.customize_file(input_file, output_file, params)</code></p>
<dd> Customize a file with specified parameters.</p>
<dt>&bull;</p>
<dd> <i>genindex</i></p>
<dt>&bull;</p>
<dd> <i>modindex</i></p>
<dt>&bull;</p>
<dd> <i>search</i></dl>
<h2>AUTHOR</h2>
<p> Dogtag PKI Project Team</p>
<h2>COPYRIGHT</h2>
<p> 2014, Dogtag PKI Team </p>
<h2>Index</h2>
<dt><a href="#lbAQ">AUTHOR</a></p>
<dd>
<dt><a href="#lbAR">COPYRIGHT</a></p>
<dd></dl>
