1 Check User ID:

2 Username and Password Initialization:

3 Lesson Plan Inquiry:

4 Level Selection and Reasoning:

5 Study Plan Request Transmission:

6 Supervisor's Requirements:

7 Study Plan Preparation:

8 Assignment Scheduling:

9 Notifications for Lesson Plan Review:

10 Assignment and Progress Tracking:

================================DATA FLOW inst=========================================

   https://t.me/c/2234131845/1057/1066




دیتا بیس سیستم جریان برنامه آموزشی:

1. User:
   - User ID
   - Username
   - Password
   - Email
   - User type (student/teacher/admin)
  
2. Courses:
   - Course ID
   - Course name
   - Description
   - Level
   - Teacher ID
   - Resources

3. Lessons:
   - Lesson ID
   - Course ID
   - Lesson title
   - Content
   - Video links
   - Audio files
   - Text files

4. Exercises:
   - Exercise ID
   - Lesson ID
   - Type of exercise (e.g., multiple choice, fill in the blanks, essay)
   - Question
   - Options (for multiple choice)
   - Correct answer
   - Explanation

5. Progress:
   - Student ID
   - Course ID
   - Lesson ID
   - Last accessed date/time
   - Completed (yes/no)

6. Teacher/Instructor:
   - Teacher ID
   - Name
   - Subject expertise
   - Contact information

7. Assignments:
   - Assignment ID
   - Course ID
   - Title
   - Description
   - Deadline
   - Submission status

8. Quizzes:
   - Quiz ID
   - Course ID
   - Title
   - Questions
   - Duration
   - Passing score

------
9. Student:
   - Student ID
   - Name
   - Age
   - Email
   - Enrolled courses
   - Progress tracking



_روابط__


۱. User (کاربر)
   - یک کاربر میتواند دانش‌آموز، معلم یا مدیر باشد که با متغیر "نوع کاربر" تشخیص داده می‌شود. هر کاربر مرتبط با یک شناسه یکتا کاربر است.

۲. Student (دانش‌آموز)
   - یک دانش‌آموز یک نوع خاص از کاربر است، با مشخصه‌های اضافی مانند نام، سن، ایمیل، دوره‌های ثبت‌نامی و پیگیری پیشرفت.

۳. Teacher/Instructor (معلم/مدرس)
   - مانند دانش‌آموز، معلم/مدرس نیز یک نوع خاص از کاربر است که دارای مشخصه‌هایی از قبیل نام، تخصص درسی و اطلاعات تماس است.

۴. Courses (دوره‌ها)
   - دوره‌ها توسط یک یا چند معلم/مدرس اداره میشوند و با شناسه یکتا دوره مرتبط هستند. این‌ها ممکن است شامل چندین درس باشند و از طریق مشخصه "دوره‌های ثبت‌نامی" به دقت خاصی به دانش‌آموزان مرتبط می‌شود.

۵. Lessons (دروس)
   - هر درس بخشی از یک دوره خاص است و حاوی محتوای خاص درسی مانند عنوان، محتوا، پیوندهای ویدیو، فایل‌های صوتی و فایل‌های متنی برای کمک به فرآیند یادگیری است.۸

۶. Exercises (تمرینات)
   - تمرینات به دروس خاص مرتبط می‌شوند و برای تقویت فرآیند یادگیری استفاده می‌شوند. آن‌ها می‌توانند انواع مختلفی داشته باشند مانند چند گزینه‌ای، پر کردن فضاها یا تمرینات مقاله‌ای.

۷. Progress (پیشرفت)
   - شهرت پیشبرد دانش‌آموزان در دوره‌ها و دروس را ثبت می‌کند. این مرتبط با دانش‌آموزان، دوره‌ها و درس‌های خاص است و ویژگی‌هایی مانند زمان و تاریخ آخرین دسترسی و وضعیت کامل شدن را پیگیری می‌کند.

۸. Assignments (تکالیف)
   - تکالیف مرتبط با دوره‌های خاص هستند و ویژگی‌هایی مانند عنوان، توضیحات و زمان حد ارسال دارند. آن‌ها می‌تواند توسط دانش‌آموزان ارسال شود و در نتیجه پیوند با کاربران ایجاد می‌کنند.

۹. Quizzes (آزمون‌ها)
   - آزمون‌ها با دوره‌های خاص مرتبط هستند و برای ارزیابی دانش دانش‌آموزان طراحی شده‌اند. آن‌ها شامل یک سری سوالات هستند، دارای مدت زمان تعیین شده‌است و برای کسب نمره قبولی برای کامل شدن نیاز است.

با تعیین این ارتباطات منطقی میان اجزا، یک۸ پایگاه داده برنامه آموزشی جامع ایجاد می‌شود که برای مدیریت صاف کاربران، دوره‌ها، دروس، تمرینات، پیشرفت‌ها، تکالیف و آزمون‌ها اجازه می‌دهد. این موارد، محیط یادگیری منظم و ارتباط موثر میان دانش‌آموزان، معلمان و مدیران را تضمین می‌کند.
