# CSC426
## System Design & Architectural Overview
This application implements a responsive, full-stack web-based authentication mechanism using an asynchronous client-server model. The frontend utilizes structured HTML5 semantic markers styled with modern user interface methodologies. To ensure data integrity and security, the system employs dual-layer validation boundaries to prevent empty or malicious payload dispatching, handling secure transaction feedback over an isolated network handshake with a Python Flask server runtime environment. Upon successful authentication, the backend securely coordinates state verification to redirect the client session to a dedicated welcome dashboard interface

## Component Layout & Interface Primitives
The frontend application layout (index.html) establishes a clean login card perfectly centered within the viewport. It incorporates the following mandatory components:

**Identification Field (Username)**: A text input region assigned for username data entry, accompanied by a dynamic error message node (#usernameError) to display immediate frontend feedback.

**Security Field (Password)**: A masked string input element ensuring sensitive credentials remain hidden during entry, paired with a dedicated error message node (#passwordError).

**Interactive Control Cluster**: An array hosting two primary triggers:

**Submit/Login Button (#loginBtn)**: Executes the validation sequence and dispatches the authenticated network request.

**Reset/Cancel Button (#resetBtn)**: Instantly purges all form values, script variables, and visible server messages.

**Integrated Communication Buffer (#formResponseMessage)**: An isolated message box that handles responsive interface communication by rendering clear success or error banners after data verification.

## Post-Authentication Landing Page (templates/welcome.html)
Upon validation success, the system dynamically shifts to an isolated dashboard container hosting:  Success Heading: High-visibility text greeting indicating secure access authorization.Security Feedback Message: Confirms backend validation clearance through the CSC426 Python service layer.  Session Termination Control (#logoutBtn): An interactive trigger that instantly invalidates the session orientation and routes the client browser back to the login interface.

## UI/UX Style Schemes 
To explore modern web interface paradigms, the application's presentation layer (style.css) was designed using  aesthetic theme.

## Matte Dark Cyberpunk Theme
This design provides a sharp, high-contrast matte framework optimized for dark-room readability.

* Canvas Stack: Uses a deep solid background (#121212) contrasted against a raised card surface (#1e1e1e) with structural dropshadow boundaries to establish clean layout depth.

* Accent Indicators: Uses vibrant amber-orange highlights (#ff9500) on execution targets and focused input borders to guide user focus.

* Physical Mechanics: Utilizes smooth transitions (all 0.2s ease-in-out) where buttons float upwards (translateY(-2px)) on hover and register physical indentation (translateY(1px)) when actively pressed.

## Operational Flow & Data Lifecycle
### Dual-Layer Validation Mechanics
* Client-Side Validation (Frontend JavaScript): Upon form submission, the local script (script.js) intercepts the event (e.preventDefault()). It flushes previous error states and strips whitespace from input values using .value.trim(). If either the username or password fields are empty, the validation engine halts the network pipeline immediately and updates the corresponding <small> error nodes with clear instructions (e.g., "Username is required.").

* Server-Side Validation (Backend Python): If local validation passes, data is transmitted to the server using the asynchronous fetch() API. As a security boundary, the Flask backend (app.py) parses the payload (request.get_json()) and re-verifies the inputs (if not username or not password:). Any bypassed or empty fields are rejected at the server level with an HTTP 400 Bad Request status response.

## Security Matching & Response Verification Matrix
The server matches the incoming credentials against its secure, backend memory states (DEMO_USER = "admin", DEMO_PASS = "password123"). The interface responds as follows

## Authentication Scenario,HTTP Status Code,Frontend UI Class,Communicating Banner Text
Credentials Match Successfully,200 OK,.success,"""Login Successful! Welcome back."" (Renders a green success alert)"
Credentials Mismatch / Wrong Login,401 Unauthorized,.error,"""Invalid username or password."" (Renders a red error banner)"
Empty Input Fields (Server Guard),400 Bad Request,.error,"""Username and password cannot be empty"""

