from distutils.core import setup

setup(name = "malipat",
      version = "0.0.1",
      description = "Test patches from a mailing list.",
      author = "Ruslan Kuprieiev",
      author_email = "kupruser@gmail.com",
      url = "https://github.com/efiop/malipat",
      scripts = ["malipat"],
      data_files = [('/etc', ['malipat.config'])]
      )
