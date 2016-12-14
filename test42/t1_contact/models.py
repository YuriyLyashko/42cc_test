from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    other_contacts = models.CharField(max_length=250)

    @staticmethod
    def get_contact_data():
        name = 'Yuriy'
        last_name = 'Lyashko'
        date_of_birth = '1986-04-10'
        bio = {'Personal_Qualities':
                        ['- desire to develop,', '- quickly learn new things,', '- initiative,', '- responsible'],
                    'Education':
                        ['2016', 'IT Education Academy courses:', 'Python base', 'Python advanced', 'Python/Django',
                         '2003-2009', 'National Aviation University,', 'Institute of Electronics and Control Systems'],
                    'Experience':['04.2009 – present time', 'Chief Power Engineer', 'MHP S.A.',
                                  'Organization of of exploitation and improvement of technical equipment:',
                                  '- organization of the working process (5 subordinates)',
                                  '- of new products monitoring;',
                                  '- analysis of the possibility of installing on a specific object;',
                                  '- calculation of efficiency, payback;',
                                  '- rationale for the use of new items to the customer;',
                                  '- choice of manufacturer, tender, purchase, delivery;',
                                  '- organization of installation and operation of equipment,',
                                  '- participation in projects,',
                                  'and etc.',
                                  '2008 – 04.2009', 'Electrical Engineer', '«Electropartner»',
                                  'Development of the equipment in accordance with the technical assignment:',
                                  '- receipt of technical specifications from the customer;',
                                  '- choice of components,',
                                  '- designing of hardware;',
                                  '- issuance of technical specifications for the installation.']
               }
        email = 'yu.i.lyashko@gmail.com'
        jabber = 'yuriylyashko@42cc.co'
        skype = ''
        other_contacts = {'Phone': '066-709-64-72','Linkedin': 'https://ua.linkedin.com/in/юрий-ляшко-27b846119'}
        return name, last_name, date_of_birth, bio, email, jabber, skype, other_contacts