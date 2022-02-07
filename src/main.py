import connect_database
import search

if __name__ == '__main__':
    apps = connect_database.select_app_id_name_slug()
    search.search(apps)
