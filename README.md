![TheWorldNftFund](https://i.imgur.com/RoiR7mc.png)

# The World NFT Fund 🌐💰

The World NFT Fund, a Django-based full-stack web application dedicated to showcasing NFT projects. This project utilizes HTML, CSS, and JavaScript for the frontend, along with Django in the backend, to provide an engaging platform for exploring various NFT initiatives.

## Features 🚀

👉 **Hero Landing Page**: An eye-catching landing page featuring animations to captivate visitors.

👉 **Basic NFT Info**: Provides fundamental information about NFT products to educate users.

👉 **Roadmap**: Presents a roadmap outlining the progression of the NFT project.

👉 **NFT Display**: Showcases various NFTs for visual appeal and engagement.

👉 **Community Discord Link**: Offers a link to the community Discord for collaboration and interaction.

👉 **Team Members**: Highlights the team members behind the project.

👉 **FAQ Section**: Answers frequently asked questions for user convenience.

👉 **Projects Page**: Displays NFT projects that can be filtered by categories for easy browsing.

👉 **Writings Section**: Features news articles and general writings, filterable by categories.

👉 **Donations Page**: Showcases donations made by the organization to support the cause.

👉 **About Page**: Provides information about the developers, who are the founders of the project.

## Usage

To use The World NFT Fund:

1. Clone the repository:

    ```bash
    git clone https://github.com/RoshisRai/TheWorldNftFund.git
    ```

2. Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Make Migrations:

    Generate migration files for the five models (Project, ProjectCategory, Writing, WritingCategory, Donation):
    ```bash
    python manage.py makemigrations projects writings donations
    ```

4. Run Migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a Superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the Development Server:

    ```bash
    python manage.py runserver
    ```

7. Adding Projects/Writings/Donations:

    To add projects, writings, or donations, log in to the admin dashboard:
    - Navigate to [http://localhost:8000/admin](http://localhost:8000/admin)
    - Enter your superuser credentials
    - Add/edit projects, writings, or donations under the respective sections

### Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`.
4. Push to your branch: `git push origin <branch_name>`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

### License

This project is licensed under the MIT License - see the `LICENSE` file for details.

### Contact

If you have any questions or feedback, please contact me at 📧 roshis.awai@gmail.com.
