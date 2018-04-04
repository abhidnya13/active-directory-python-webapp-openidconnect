# ADAL Python Web App Sample

This sample shows how to build a Python Flask Web-App that uses ADAL Python to obtain access token for the MS Graph API from AAD.

## QucikStart 

### Step 1: Register your application in an Azure AD Tenant

- To use this sample you will need an Azure Active Directory Tenant. If you're not sure what a tenant is or how you would get one, read [What is an Azure AD tenant?] (https://technet.microsoft.com/library/jj573650.aspx) or [Sign up for Azure as an organization] (https://docs.microsoft.com/en-us/azure/active-directory/sign-up-organization). These docs should get you started on your way to using Azure AD. You can follow the instructions here to register the app with Azure AD.

- To set up the app to authenticate users, first register it in your tenant by doing the following:
  1. Sign in to the [Azure portal] (https://portal.azure.com).
  2. On the top bar, click your account name. Under the **Directory** list, select the Active Directory tenant where you want to register the app.
  3. Click **All services** in the left pane, and then select **Azure Active Directory**.
  4. Click **App registrations**, and then select **Add**.
  5. Follow the prompts to create a **Web Application and/or WebAPI**.
     - **Name** describes the app to users.
     - Sign-On URL is the base URL of the app. 
  6. After you've completed the registration, Azure AD assigns the app a unique application ID. Copy the value from the app page to use in the next sections.
  7. From the Settings -> Reply URLs page for your application, update the Reply URL for the application. It is of the format http://localhost:<PORT>/getAToken. The sample App uses PORT 5000 since it is the default port on which Flask web Apps run.
  8. Generate a key(client secret) from Settings-> Keys page of your application. GENter a key description and duration for the key and click Save. The key value will be displayed. Copy and store the value from the app page to use later for configuration.
  9. You will also have to grant permissions to access the Microsoft GRaph API by going to Settings-> Required Permissions. Click on Add. Select the API(Sample App uses Micrsoft Graph API) and select the required permissions(Sample App uses sign in and read user profile).


### Step 2: Download Python(2.7 and above) 
To successfully use this sample, you need a working installation of Python 2.7 and above.
You also will have to install Python Flask.

### Step 3: Download the sample application.

From your shell or command line:
```
$ git clone https://github.com/Azure-Samples/active-directory-python-webapp-openidconnect.git
$ cd active-directory-python-webapp-openidconnect
```

### Step 4: Update the config file 

Open the config.py file and fill in the necessary details as instructed. 

### Step 5: Run the program

Run app.py from shell or command line :
```
python app.py
```
Follow the sign in process to complete the logging.

### And you're done!
