from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import redis, json
from django.conf import settings

class ScratchNews(APIView):
    def get(self, request):
        conn = redis.StrictRedis.from_url(settings.CACHES["default"]["LOCATION"])

        news_data_redis = conn.get('news')

        if news_data_redis:
            return Response(json.loads(news_data_redis.decode('utf-8')), status=status.HTTP_200_OK)
        else:
            news_data = [
                {
                    'title': '유진기업, 레미콘 업계 안전문화 확산 위해 세 번째 안전가이드 북 발간', 
                    'preview': '[서울=뉴스핌] 송은정 기자 =유진그룹의 모기업 유진기업이 레미콘 업계의 안전한 근로환경 정착에 힘쓰고 있다. 썸네일 이미지.', 
                    'author': '뉴스핌', 
                    'date': '2024. 4. 23.', 
                    'thum': 'data:image/jpeg;base64,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', 
                    'link': 'https://www.newspim.com/news/view/20240423000060'
                },
                {
                    'title': '산업 안전사고, LOTO 시스템으로 예방한다', 
                    'preview': 'LOTO 프로그램에는 기기별 절차 및 LOTO 담당 직원에 대한 연례 감사가 포함되는데, 기기 변경이 발생할 때, 이를 포착하는 시스템을 구현하면 감사 업무...', 
                    'author': '헬로티', 
                    'date': '2022. 4. 25.', 
                    'thum': 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAFwAXAMBIgACEQEDEQH/xAAcAAADAQEBAQEBAAAAAAAAAAAEBQYHAwIBCAD/xABCEAACAQIEAgYECgcJAAAAAAABAgMEEQAFEiEGMRNBUWFxgQciMqEUIyRCYpGxwdHwFTNSU3OysxYmY3KCk6PCw//EABkBAQEBAQEBAAAAAAAAAAAAAAQFAwIBAP/EACURAAICAQQBAwUAAAAAAAAAAAECAAMRBBIhMVEyQWEFEyJC0f/aAAwDAQACEQMRAD8Ap4ACRhbxaQOGsxI/dr/UTDCmNhfCvjVrcLZgevTGP+VMMbqTk7EzTMTahpb/ALsfYMK5EtfSWsOR78McxN6Wn7ox/KMeMsqIKepZpnKMABHIATp7T49+D2NgZjqlycTT6DPcsyHKaWGolklqlp0ApaddUi+qPaA9nztzwrHHsVVJUfD6aqRHOmGFCoVVsPaJ2Jvfe2BODszyyllKGCSSNpW+ORLl2O9rc+Qv54p+JeC4c7ggky4RUm/rkCwIPdyxNp09dbbiMk+ZQcF04MX5JxTk9Uz5ZXU4og1xHOzjS9+1wBpP5vj1nM9f8GDw5lDVUOkrJGq9Nq+iQxa4I78Ka7hGNIKukglleopmJBJ9tbLbbq31e7ESgkoZgweZIS120nSxt9+FsEuGCIc1tSciOMj0GqqWiTQjKrBey5JthjmVGlXTssiFlVS3q8wR14CyI6pp5HIDSWKjUCbdpth1Oejoap+yFvsthS4xAvkNIiOGMFdNyGCH1h9FicBkjDFkEbRJ+yi3/wBsn78K254+M1WbrA1188KeN2/uvWj+F/VTDOFrDCfjU34aq79Zj/qKfuxq3UEnqEzerOqCEbbKNv8ASuBNN99CHzP44MiFIxkFa8ygQEw9CAbyaV0g3+bzvgcw+17e30B39/d+evGNHEuOCKaFchqHZo+mkqldYUJLMEtfbt3PljTaKqjelUqwKabqcYBRrLFVxvSg/CAfU1CwbuO/I2xos3G2T0mXwrTyPUzyKGaKJLWbrG/LfqwW1DniUKLF2YPGJaGminSSX2WkOl3Hzl78SHFHBsMzxfBpUjnmvrBF+q4P2Dzxy4f9IDVlaMvzGi+D9KPiijahuLgHbnbF1lES11VDWGImKIMpuOTg/n3YzVGU4nT2Iy59piuZcP5vwukVZWCGLpJNMa6hrbY76ezxtilyfKczzqJaOoSOjNVG2hi2v1QAeQ69+V+QPZjj6TVqcw4kkqArPT04WFQOV/ne828sVNPW6cno85SzPQVCTSgG3qEGOT6ldjbuxqbCGCgzhdMGqZ2HPtI7iDgLPMs1VEcaVcSruILlwAlvZ5nyviCNieYx+q5NEq2YAqRfccxiJzr0b5HmmYPWOJ4Xk3cQSaVY9trc8IHUBnBgsT7YU8atbhuo73j/AJhgnL5dUMZvquo37dsBcaMDw5Nf94n242bqDrH5SCoZFEk+sgfJmAuVG+kdv3b4FIHJQlu1inf+H52wVlWWT5vVmnp2jj0xmSSWVtKRotrsT5gbduDk4VrJaueGKoppY4EV3mjc6SrXta4G+3Lb7Ln3ru255lEIxXIHEU0zMJ4ihhQjrkCBb9+3LHxKjS5YpGytYMukAMBbbtHiN8PqfgyslnaNqumQBEcMXFyGJA69uRwXknBRqagSVVRG9OjNdIjctpYrYnq5fV2Y8dlUZM9qra19i9w7giHh+poamqny8DMYZGaPWJGiC7WI+bcXPftfGrUWZpTcJQVNukaOMxqp2Mkl9IHmevxOIFZIqeplo1gYQ/BtEQjX1VuwuCer2R9ZxS5VG1ZDT6haKJmeJDyF+bePO3d44P8AfzzHtoNp2+wxk/ycqTLYp6BoKgCRzFeR9PtuxJZvMknH0ZHFRU80KHVS1cbRyRt9IWOHkdOySlrXW1ufVjmUJWSJlOocmPUMYY5zGCz9R1PPC9VLVZBRioN50i0kjrK+qw+sHDEOrDdlBGxucJeHLrT11ML3grnUEfN12e483wRU1EaSlaiKpMg5mniLKfq5HuxQU5EgWLtYiQWUn5LDb9gYE41c/oJh2yp9+OXD2aw1cZgUFJYRbST7Q5XGPPGcl8mt/ir9jYQeVg1BFkmeG60UlXUdIsMkE0DRTRyuUDoSvJhyYEAg92GVDnE1NmM5jFHOkgU9LOvTCIBtrnUo5WufAWvthJlENJUTVCV05hUQO0RCFtUm2lbDt37tsFS01GJhBQ1IKGjX4S7x6Aj3uwOojkQu/I4PsXduxzHCxwuwHgx/QZ/ItbL0sFJHNKI44vkoCWQltXtHb1ud97DFJkYlheeCVSrqvIpp2YB728G+7HHgnhWoemqJK2BRHM8fRtJHewVbXABPPbn2crc9EpMjo5at5plZ5o41VW1Ebb88Y6kZQAeYnQXLRYzt4kVSZdLUyxGNWYMw1nqJPf2DbF5lGUJDARI5YjY6RYYWyy0WU0Zp2dYbsWCpa7Ed3h1nBFFnc09MsiIsauxsDuRibQxL8jiUNRdfqFyowsfCkgFvVJ262OJ+QlMwfsuVscezmFUZwrTNax2G2BJpD0jOxJJ3ucLLZmVNLqTuPc55UOj4hzOAWC1FPHUxr2upKt7hHhvSQhoFYbark9+EEsgi4pyia28okpL/AOZdf/linpP1IA6iR78LrOVk/UrttM/MdJWS0dQlRDp6RCbauXni/fIanibh+knjnSneUCUoy36iO3kb3xmwdRKC4JQH1gDYkde/Vi8o/SJBTwqiZe8SKAoWMggDs6sdsWxxMkRM5aeqP0dVMTsZa2JgVKlejO9/PBWXcHDLqxKqsgirzGgCI91QMPnEb6vDbHuL0jUTbukiHvX8Mfaj0g0JQ2MjdwQ4xO+JQV8/M03JsxSenCzKsUyrcqOsd2J/jOskSeM0s0sI0WLJIVufL874lKXi1YSmaPUU8dNGGIjEgeSYkW0hQdjv19mEGR5xV51nVbPWSMdaApHfaMX5D8cZ3hjUSYr6eKxq1HeZTxs9TpZpGeQHTZtzbFZRJ0dLAp2KqPfhNk1NBFFrkcdM5JI7B1YdxMsiFUYMQOQOB1iWtWwP4qOBOzn49T2EjH9KdQNuZOFHED5m1Mf0KYRVMVIM3IDr88R8nFXEmR1EQ4hoEelka3SRAAnwINr9xthKqW6k53FZG6V2bytG0NTHb5LNDJc9msA+5jioGZUlEOiqKqKNz61pHAJ79+++IOszehrOH6yopqiOZehaRkDWYWsbEcxyxmde1XxBWz5jWvrlkc+0AdA6lF+QGN6DtU5gdev3HUpzxGdHllF0UbmAMxAJ1G+/hjnxBTU8dBE0UEaMZrEqu9tJwdRfqkHcMB8Qm9DD/G/64awG2REJNg5k2QA5A5b88fH2BJ54JhjVkkka5YBrYGcXv4YxjSIXmNLHT1jxR6gFVPa3NyoJ95w14QCx5mDc/GRulvDSfxwoqqmSqdZZAobSAdItfbDfgwj+0uTKyq6tVFWVhcEFQDfGNwzWw+Iii0U2JZjoyvhrauWc00UYmRRsBGWa3YLYp8toM2mhBTLmTRurM4Qj698NYj0M0sUQVVifUoAtbci3hth5lRJuL82OItdpZgJUu+ql/Sgmc8QxcXyzw0GU5d0JdS0lb0ilAOzVyX7ezGX5sxjrHh/Sb15U+vLdtBbr0kk6hf51hfsxuvpLlkp/R3mksDmNyViLL1oZQpHmCRjLOMsppMqbI8po0Kwyqss0hsZJXYgXY9wJAAsNztirQxwMyXbY1zZMkQb/AI4Kpq+ppY+jgkAUm5BUHfFNX8OZcsTdEskbKCdSvcm3jfEgIwb7nmR78bpYtgn1+ms05G49+J//2Q==', 
                    'link': 'https://www.hellot.net/news/article.html?no=67640'
                }
            ]

            conn.set('news', json.dumps(news_data))
            conn.expire('news', 10800)
            return Response(json.loads(conn.get('news').decode('utf-8')), status=status.HTTP_200_OK)
