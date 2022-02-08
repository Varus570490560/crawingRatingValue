import connect_database
import search_at_mc

if __name__ == '__main__':
    apps = connect_database.select_app_id_name_slug()
    search_at_mc.search_percentage(apps)
