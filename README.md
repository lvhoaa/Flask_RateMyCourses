# RATE MY COURSES -- See reviews, get advice, and rate your college courses 

RateMyCourses is a web application built with Flask to serve as a platform for students to see and create reviews about university courses.

[Django version](https://github.com/lvhoaa/RateMyCourses)

## Table of Contents

- [Project Overview](#project-overview)
- [Illustrations](#illustrations)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Project Overview 

Knowing choosing the right course in college is difficult, RateMyCourses aims to help students find their best-fit courses by reading reviews and advice from past students. 

Key features of RateMyCourses project includes: 
- Flask-based web application for reading and making reviews
- Designed database with one-to-many relationships using ORMs
- Integration with OpenAI API for crafting high-quality summary from course reviews.
- Develop star-rating system on multiple aspects of a course: quality, grading, and difficulty.
- Support profanity detection to obtain comments of highest quality
- Support login/logout/registration system to validate users

## Illustrations

![image](https://github.com/lvhoaa/RateMyCourses/assets/87745938/66926dba-4887-4c44-83cc-6a860a65f53c)

![image](https://github.com/lvhoaa/RateMyCourses/assets/87745938/6759cffa-f29c-4d0e-85b0-4bdba3f97f94)

![image](https://github.com/lvhoaa/RateMyCourses/assets/87745938/d5050169-050b-41d8-8c31-7e9614c0205a)

![image](https://github.com/lvhoaa/RateMyCourses/assets/87745938/d3ed05a5-b416-49c3-8cba-3548990b4c01)

## Installation

1. Clone the repository or download the source code.
   ```bash
   git clone https://github.com/lvhoaa/RateMyCourses.git
2. Create a virtual environment (optional but recommended).
    ```bash
    python3 -m venv myenv
3. Activate the virtual environment.

- On Linux/macOS:
    ```bash
    source myenv/bin/activate

- On Windows:
    ```bash
    myenv\Scripts\activate

4. Install the dependencies.
    ```bash
    pip install -r requirements.txt

5. Perform any additional setup steps required, such as setting up a database or configuring environment variables.

## Usage

To run the RateMyCourses server, follow these steps:

1. Make sure your virtual environment is activated.

2. Run the development server.
    ```bash
    python main.py
4. Open a web browser and visit http://localhost:5000 to access the application.

5. Read course reviews and make high-quality ratings 

## Configuration
- The RateMyCourse project leverages the OpenAI API for summarizing course comments. To use the OpenAI API, you need to obtain an API key from OpenAI and configure it in the project.

- Obtain an API key from OpenAI by following their documentation.

- Configure the API key in the project's main/chatgpt.py file. 

## Contributing
- Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request. For major changes, please discuss them first in the project's issue tracker.

## License
- This project is licensed under the MIT License. You can find the full license text in the LICENSE file.
