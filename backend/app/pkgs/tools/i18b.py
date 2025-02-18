import gettext
from flask import session

from config import LANGUAGE

def getCurrentLanguageName():
    try:
        language = session['language']
    except Exception as e:
        language = LANGUAGE

    if language == "en":
        return "English"
    else:
        return "Chinese"

def getI18n(domain):
    try:
        language = session['language']
    except Exception as e:
        language = LANGUAGE

    if language is None:
        language = LANGUAGE

    translate = gettext.translation(domain=domain, localedir="./i18n", languages=[language])
    translate.install()
    i18n = translate.gettext
    return i18n

def getFrontendText():
    _ = getI18n("frontend")
    return {
        "title": _("DevOpsGPT"),
        "change_language": _("切换为中文"),
        "start": _("Start"),
        "more_operations": _("More"),
        "hello": _("Hello"),
        "login": _("Login"),
        "logout": _("Logout"),
        "error":_("ERROR"),
        "service_modification_item_empty":_("The services involved are not analyzed. Check whether the application architecture information is accurate"),
        "ai_think": _("Thinking..."),
        "ai_start_1": _("Hello, I am the AI-assisted code development assistant, please select the"),
        "ai_start_2": _("to start the development task!"),
        "ai_select_app": _("I need to develop requirements in the"),
        "ai_selected_app_1": _("Task APP"),
        "ai_selected_app_2": _("Task ID"),
        "ai_selected_app_3": _("Task repo"),
        "ai_selected_app_4": _("Task branch: Based on"),
        "ai_selected_app_5": _("to development"),
        "ai_selected_app_6": _("Now, please tell me the requirements that need to be completed, describing them in as much detail as possible."),
        "ai_requirement_clarify_1": _("Development requirements overview: "),
        "ai_requirement_clarify_2": _("Development requirements details: "),
        "ai_requirement_clarify_3": _("The requirements document has been generated, and the interface document will be generated after confirmation: "),
        "ai_requirement_clarify_4": _("In order to better understand the requirements, I also need to confirm the following questions: "),
        "ai_api_clarify_1": _("The interface documentation has been generated, and once confirmed, the analysis of how to modify the program code will begin: "), 
        "ai_api_clarify_confirm": _("Confirm interface document."),    
        "ai_api_subtask_1": _("Analyzing how to modify the"),    
        "ai_api_subtask_2": _("code according to the requirement description, it is expected to take 1-6 minutes, please wait..."),  
        "ai_api_subtask": _("According to the above development tasks and the product database, I analyze that the following contents need to be modified:"), 
        "start_ci": _("Start CI"),  
        "submit_code": _("Submit code"),  
        "auto_check": _("Auto check"),  
        "modify_file": _("Modify file"),  
        "reasonfor_for_modification": _("Reason for modification"),  
        "adjust_code": _("Adjust code"),  
        "review_code": _("Review code"),  
        "status": _("Status"),  
        "app": _("APP"),
        "select_app": _("Select APP"),
        "requirement_description": _("Requirement description"),
        "operation": _("Operation"),
        "submit": _("Submit"),
        "ok": _("Ok"),
        "edit": _("Edit"),
        "close": _("Close"),
        "cancel": _("Cancel"),
        "retry": _("Retry"),
        "restart": _("Restart"),
        "question": _("Question"),
        "answer": _("Answer"),
        "initial_code": _("Initial code"),
        "self_check": _("Self check"),
        "compile_check": _("Compile check"),
        "fix_compile_check": _("Fix Compile check"),
        "static_scan": _("Static scan"),
        "fix_static_scan": _("Fix Static scan"),
        "no_problem_this_file": _("No problem found in the current file, refer to other solutions:"),
        "backend_return_error": _("The back-end service returns an exception. Contact the administrator to check the terminal service logs and browser consol."),
        "start_cd": _("Start deployment"), 
        "start_task": _("Start task"), 
        "requirement_list": _("Requirement List"), 
        "app_list": _("APP List"), 
        "setting": _("Setting"), 
        "create_new": _("Create new"), 
        "back_to_list": _("Back to list page"),
        "app_name": _("APP name"), 
        "app_intro": _("APP introduction"), 
        "app_base_branch": _("Base branch"), 
        "app_feat_branch": _("Feature branch"), 
        "service_name": _("Service name"), 
        "service_role": _("Service role"), 
        "service_language": _("Language"), 
        "service_framework": _("Framework"),
        "service_libs": _("Dependency library"),
        "app_sub_service": _("APP sub service"),
        "git_path": _("Git path"),
        "ai_code_analysis": _("AI code analysis"),
        "service_api_type": _("API type"),
        "service_api_path": _("API path"),
        "service_database": _("Service database"),
        "service_code_struct": _("Service code struct"),
        "requirement_id": _("Requirement ID"),
        "requirement_origin": _("Requirement name"),
        "requirement_status": _("Requirement status"),
        "requirement_user": _("Requirement owner"),
        "requirement_completion": _("Requirement completion rating"),
        "requirement_satisfaction": _("Requirement satisfaction_rating"),
        "opensource_version_1": _("Historical requirement recovery is not supported at this time, please visit workspace to obtain the code results"),
        "notice": _("Notice"),
        "username": _("Username"),
        "password": _("Password"),
        "register": _("Register"),
        "email": _("Email"),
        "tenant_name": _("Company Name"),
        "tenant_status": _("Company Status"),
        "tenant_description": _("Company Description"),
        "tenant_billing_type": _("Billing type"),
        "tenant_billing_quota": _("Billing quota"),
        "tenant_created_at": _("Created"),
        "tenant_billing_end": _("Plus expiry"),
        "employee_count": _("Employee count"),
        "industry_type": _("Industry type"),
        "change_tenant": _("Switch Tenant"),
        "tenant_member_count": _("Member Count"),
        "create_tenant_notice": _("Please ensure that the information is accurate and we will review it within 24 hours to activate your account."),
        "create_user_notice": _("In order to protect your rights, please ensure that the information is accurate."),
        "enter": _("Enter"),
        "show_tenant": _("Details"),
        "members": _("Members"),
        "country": _("Country"),
        "role": _("Role"),
        "phone": _("Phone Number"),
        "add_member": _("Add member"),
        "invite": _("Invite"),
        "billing": _("Billing"),
        "bill_type": _("Bill type"),
        "bill_user": _("Operating user"),
        "bill_date": _("Billing date"),
        "remarks": _("Remarks"),
        "operate": _("Operate"),
        "git_provider": _("Git provider"),
        "git_url": _("Git URL"),
        "git_token": _("Git token"),
        "git_username": _("Git username"),
        "git_email": _("Git email"),
        "ci_token": _("CI Token"),
        "ci_api_url": _("CI API URL"),
        "ci_provider": _("CI provider"),
        "cd_provider": _("CD provider"),
        "ACCESS_KEY": _("ACCESS_KEY"),
        "SECRET_KEY": _("SECRET_KEY"),
        "configuration": _("Configuration"),
        "config_name": _("Config name"),
        "app_cd_config": _("Associated CD Config"),
        "app_ci_config": _("Associated CI Config"),
        "app_git_config": _("Associated Git Config"),
        "my_role": _("My Role"),
        "others_1": _("The tenant does not exist or is abnormal"),
        "others_2": _("Insufficient authority."),
    }