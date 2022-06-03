from postal_address import PostalAddress

if __name__ == '__main__':
    try:
        postal_address_service = PostalAddress()
        postal_address_service.get_zip_code()
        postal_address_service.remake()
    except KeyboardInterrupt:
        print('\nPrograma finalizado!')
