<h1>Python Site Blocker</h1>

A Python tool to block access to specific websites for a specified amount of time, only allowing access via an unblock code that is sent to your email after the period of time specified has passed.

<h1>Modules</h1>

<ul>
    <li>os</li>
    <li>random</li>
    <li>time</li>
    <li>smtplib</li>
    <li>MIMEText</li>
</ul>

<h1>Current Features</h1>

<ul>
    <li>Site blocking is achieved by the website address being added to the systems host file with the loop back address of 127.0.0.1</li>
    <li>Hours of downtime and entry of the unblocking code is achieved through prompts and user input via the terminal</li>
    <li>Connection and the use of the smtplib in order to send the email with the unblocking code (current setup uses the same address to create, send and receive the unblocking code - further developments will allow a stand alone distribution email account and user input to specify their email address for a code to be sent too).</li>
    <li>Site unblocking is achieved by ensuring the code that is distributed via email matches what the user inputs. At this point the hostfile is again updated to remove the additional routing.</li>
</ul>

<h1>Future Plans</h1>

<ul>
    <li>As specified above, the creation of a single distribution email account, with possibility for the user to enter their own email address to receive the unblocking code.</li>
    <li>Development of UI (possibly using Flask), to move terminal interface to browser.</li>
    <li>Possible development to move this into a Chrome extension, to be accessed and used via a browser.</li>
</ul>