from blog.models import Post
from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):
    help="This command insert post data"

    def handle(self, *args: Any, **options: Any):
        # delete the existing data
        Post.objects.all().delete()

        title = [
        "10 Tips for Better Time Management",
        "A Beginner's Guide to Meal Prepping",
        "How to Start a Morning Routine That Sticks",
        "The Basics of Personal Finance",
        "Why Reading Every Day Changes Your Life",
        "Simple Home Workouts for Busy People",
        "How to Stay Productive While Working From Home",
        "A Guide to Minimalist Living",
        "Top 5 Destinations for Solo Travelers",
        "Understanding the Basics of Investing",
        "How to Build Healthy Sleep Habits",
        "The Art of Effective Communication",
        "Beginner's Guide to Growing Your Own Vegetables",
        "How to Overcome Procrastination",
        "5 Ways to Reduce Stress Daily",
        "The Importance of Setting Realistic Goals",
        "A Simple Guide to Journaling",
        "How to Improve Your Focus and Concentration",
        "Budget-Friendly Meal Ideas for the Week",
        "Tips for Building Better Habits",
        ]

        content = [
        "Learn how to prioritize tasks, avoid distractions, and make the most of your day with these simple time management strategies.",
        "Meal prepping can save you time and money while helping you eat healthier. Here's how to get started as a beginner.",
        "A consistent morning routine can set the tone for your entire day. Discover the habits that make mornings easier.",
        "Understanding budgeting, saving, and spending wisely are the first steps toward financial freedom.",
        "Reading daily boosts knowledge, reduces stress, and improves focus. Here's why you should make it a habit.",
        "You don't need a gym to stay fit. These simple workouts can be done at home in under 30 minutes.",
        "Working from home comes with unique challenges. Learn how to stay focused and productive throughout the day.",
        "Minimalism isn't about owning less for the sake of it — it's about making room for what truly matters.",
        "Traveling alone can be one of the most rewarding experiences. Here are five destinations perfect for solo explorers.",
        "Investing doesn't have to be complicated. This guide breaks down the basics for beginners looking to grow their money.",
        "Quality sleep is essential for health and productivity. Learn how to build habits that improve your sleep quality.",
        "Clear and effective communication can improve relationships, both personal and professional. Here's how to master it.",
        "Growing your own vegetables is easier than you think. Start your first garden with these beginner-friendly tips.",
        "Procrastination affects everyone at some point. Learn practical strategies to overcome it and get things done.",
        "Daily stress can take a toll on your mental health. Try these five simple techniques to manage it effectively.",
        "Setting realistic, achievable goals is key to long-term success. Learn how to set goals that actually stick.",
        "Journaling is a powerful tool for self-reflection and mental clarity. Here's a simple guide to get started.",
        "Struggling to stay focused? These techniques can help improve your concentration and productivity.",
        "Eating well on a budget is possible with the right planning. Check out these affordable meal ideas for the week.",
        "Building better habits takes time and consistency. Learn the science-backed strategies that actually work.",
        ]

        img_url = [f"https://picsum.photos/id/{i}/800/400" for i in range(1, 21)]

        for t, c, img in zip(title, content, img_url):
            Post.objects.create(title=t, content=c, img_url=img)
        self.stdout.write(self.style.SUCCESS("Completed inserting data!")) 
