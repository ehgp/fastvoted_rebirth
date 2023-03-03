"""Main."""

import datetime as dt
import json
import os
import sqlite3
import sys
from pathlib import Path

import requests
import yaml

import log


def _load_config():
    """Load the configuration yaml and return dictionary of setttings.

    Returns:
        yaml as a dictionary.
    """
    config_path = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(config_path, "sites.yaml")
    with open(config_path, "r") as config_file:
        config_defs = yaml.safe_load(config_file.read())

    if config_defs.values() is None:
        raise ValueError("sites yaml file incomplete")

    return config_defs

#     async updatePlatformData({ state, commit }, { platform, forced, url }) {
#       const platformConfig = state[platform];
#       const threshold = platformConfig.cache;
#       const lastUpdate = platformConfig.updated_at;
#       const now = new Date();

#       if (!lastUpdate || now - lastUpdate > threshold || forced) {
#         const response = await fetch(url);
#         let data = await response.json();
#         if ('responseDataKey' in platformConfig) {
#           data = data[platformConfig.responseDataKey];
#         }
#         commit('setPlatformData', { platform, data });
#       }
#     },
#   },
#   getters: {
#     getPlatformByIndex: state => cardIndex => state.settings.cards[cardIndex],
#   },
# });
# def update_engine(cache):
#   """Update according to how long the cache has been active."""

# def create_dbs():
#     """Create the databases."""
#     logger.info("Creating Tables for each news source")
#     create_table_github = """CREATE TABLE IF NOT EXISTS github \
#     (repo text, owner text,  link text, \
#     description text, stars text, todayStars text, language text)"""
#     create_table_hackernews = """CREATE TABLE IF NOT EXISTS hackernews \
#     (title text, link text, score text, age text, commentCount text, threadLink text)"""
#     create_table_producthunt=
#     create_table_designernews=
#     create_table_devto=
#     create_table_lobsters=
#     create_table_tabnews=
#     tables = [create_table_github, create_table_hackernews, create_table_producthunt, create_table_designernews, create_table_devto, create_table_lobsters, create_table_tabnews]
#     with sqlite3.connect("db/news.db") as con:
#       cur = con.cursor()
#       for table in tables:
#         logger.info("Creating Table tickers")
#         cur.execute(table)
#         con.commit()
#       con.close()

# def insert_entry(table, columns, values):
#     """Insert a row of data into the table."""
        # GITHUB {'repo': {'rawName': 'mrsked / mrsk', 'owner': 'mrsked', 'name': 'mrsk', 'link': '/mrsked/mrsk', 'description': 'Deploy web apps anywhere.'}, 'stars': {'count': 2381, 'link': '/mrsked/mrsk/stargazers'}, 'forks': {'count': 69, 'link': '/mrsked/mrsk/forks'}, 'todayStars': 483, 'language': {'is': 'Ruby', 'color': '#701516'}}
        # HACKERNEWS {'title': 'Redox OS – A Unix-Like Operating System Written in Rust', 'link': 'https://www.redox-os.org/', 'siteString': 'redox-os.org', 'score': '61 points', 'user': {'name': 'jitl', 'link': 'user?id=jitl'}, 'age': '1 hour ago', 'commentCount': '8 comments', 'threadLink': 'item?id=35005259'}
        # PRODUCTHUNT  {'comments_count': 967, 'id': 381299, 'name': 'trumpet', 'product_state': 'default', 'tagline': 'Build collaborative buyer journeys in 30 seconds', 'slug': 'trumpet-2', 'votes_count': 972, 'day': '2023-03-02', 'category_id': None, 'created_at': '2023-03-02T00:01:00.000-08:00', 'current_user': {'voted_for_post': False, 'commented_on_post': False}, 'discussion_url': 'https://www.producthunt.com/posts/trumpet-2?utm_campaign=producthunt-api&utm_medium=api&utm_source=Application%3A+Devo+%28ID%3A+6289%29', 'exclusive': None, 'featured': True, 'ios_featured_at': False, 'maker_inside': True, 'makers': [{'id': 0, 'created_at': '1969-12-31T16:00:00.000-08:00', 'name': '[REDACTED]', 'username': '[REDACTED]', 'headline': None, 'twitter_username': None, 'website_url': None, 'profile_url': 'https://www.producthunt.com/', 'image_url': {}}, {'id': 0, 'created_at': '1969-12-31T16:00:00.000-08:00', 'name': '[REDACTED]', 'username': '[REDACTED]', 'headline': None, 'twitter_username': None, 'website_url': None, 'profile_url': 'https://www.producthunt.com/', 'image_url': {}}, {'id': 0, 'created_at': '1969-12-31T16:00:00.000-08:00', 'name': '[REDACTED]', 'username': '[REDACTED]', 'headline': None, 'twitter_username': None, 'website_url': None, 'profile_url': 'https://www.producthunt.com/', 'image_url': {}}], 'platforms': [], 'redirect_url': 'https://www.producthunt.com/r/e0b344d814495e/381299?app_id=6289', 'screenshot_url': {'300px': 'https://url2png.producthunt.com/v6/P5329C1FA0ECB6/c8f88f5fc6729fc1d1d17cebafbeb0e1/png/?max_width=300&url=https%3A%2F%2Fwww.sendtrumpet.com%3Fref%3DProductHunt', '850px': 'https://url2png.producthunt.com/v6/P5329C1FA0ECB6/2d2fa713f810101ed243375fd904b40a/png/?max_width=850&url=https%3A%2F%2Fwww.sendtrumpet.com%3Fref%3DProductHunt'}, 'thumbnail': {'id': 'Thumbnail-381299', 'media_type': 'image', 'image_url': 'https://ph-files.imgix.net/04561967-d452-4239-b43c-a278131c1835.png?auto=format&fit=crop&h=300&w=300', 'metadata': {'table': {'url': None, 'kindle_asin': None, 'video_id': None, 'platform': None}}}, 'topics': [{'id': 71, 'name': 'Sales', 'slug': 'sales'}], 'user': {'id': 0, 'created_at': '1969-12-31T16:00:00.000-08:00', 'name': '[REDACTED]', 'username': '[REDACTED]', 'headline': None, 'twitter_username': None, 'website_url': None, 'profile_url': 'https://www.producthunt.com/', 'image_url': {}}}
    # DESIGNER NEWS {'id': '129503', 'href': 'https://api.designernews.co/api/v2/stories/129503', 'links': {'user': '105687', 'comments': ['335241', '335242'], 'upvotes': ['568317', '568318', '568319', '568320', '568321', '568322', '568323', '568324', '568325'], 'downvotes': []}, 'created_at': '2023-03-02T13:55:54.000Z', 'updated_at': '2023-03-02T15:38:41.000Z', 'title': '12 Best Designed Websites of 2023', 'badge': 'show', 'comment': None, 'comment_html': None, 'comment_count': 2, 'category': 'show', 'pinned_at': None, 'url': 'https://kisirehberi.com', 'sponsored': False, 'vote_count': 10, 'hostname': 'kisirehberi.com', 'twitter_handles': []},

#     con = sqlite3.connect("db/news.db")
#     placeholders = ", ".join("?" * len(values))
#     insert_table = "INSERT INTO %s ( %s ) VALUES ( %s ) ON CONFLICT IGNORE" % (
#         table,
#         columns,
#         placeholders,
#     )
#     logger.info("Inserting a row of data")
#     cur.execute(insert_table, values)
#     con.commit()
#     con.close()

def get_data(url):
    """Receive the content of url, parse it as JSON and return the object.

    Args:
      url(str) : URL to fetch.

    Returns:
      dict : The JSON response.
    """
    response = requests.get(url)
    data = json.loads(response.text)
    return data


if __name__ == "__main__":
    logger = log.setup_logger(__name__)
    logger.info("Starting main.py")
    sites = _load_config()["sites"]
    site_links = [sites["github"]["backup"], sites["hackernews"]["backup"], sites["producthunt"]["backup"], sites["designernews"]["backup"], sites["devto"]["backup"], sites["lobsters"]["backup"], sites["tabnews"]["backup"]]
    data = get_data(sites["designernews"]["backup"])
    print(data)
    logger.info("Ending main.py")
