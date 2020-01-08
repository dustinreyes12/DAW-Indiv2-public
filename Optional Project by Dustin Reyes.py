#!/usr/bin/env python
# coding: utf-8

# In[1]:


import base64
import os
import dash
import joblib
import pickle
import pandas as pd
import numpy as np
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go
from IPython.display import display, IFrame, HTML
from dash.dependencies import Input, Output, State

df_unemployment = pd.read_csv('data/Unemployment.csv')
df_unemployment = df_unemployment.dropna(axis=1, how='all')
to_drop = ['Indicator Name',  'Indicator Code']
df_unemployment.drop(to_drop, axis=1, inplace=True)
df_unemployment.head()


image_filename = 'data/combined2.jpg'
image_filename2 = 'data/causes.png'
image_filename3 = 'data/me.jpg'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())
encoded_image3 = base64.b64encode(open(image_filename3, 'rb').read())

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Related Study",
                                href="https://hrdailyadvisor.blr.com/2019/08/05/recruiting-and-the-effects-of-low-unemployment/"))
    ],
    brand="The Future of Human Resources: HR Analytics and Global Unemployment ",
    brand_style={'font-weight': 'bold', 'font-size': '28px'},
    brand_href="/",
    sticky="top",
)

body = dbc.Container([
    html.Br(),
    dbc.Jumbotron(
        [
            html.H1("HR Analytics", className="display-3"),
            html.P(
                """
                Human resource analytics (HR analytics) is an area in the 
                field of analytics that refers to applying analytic processes
                to the human resource department of an organization in the 
                hope of improving employee performance and therefore getting 
                a better return on investment. HR analytics does not just deal
                with gathering data on employee efficiency. Instead, it aims 
                to provide insight into each process by gathering data and 
                then using it to make relevant decisions about how to 
                improve these processes.
                
                """,
                className="lead", style={'text-align': 'justify'}
            ),

            html.P(
                """
                To be able to understand HR Analytics, let us first observe
                the global unemployment rates throughout the recent decades.
                This shall enable use to understand the stakes and effects
                of unemployment to the future of Human Resources.
                """,
                className="lead", style={'text-align': 'justify'}
            ),
            html.Hr(className="my-2"),
            html.P(
                """
                In this web application, we explore the HR analytics through
                descriptive and predictive analytics. The features of this 
                web application includes predictive analytics on
                talent acquisition, predictive analytics on employee attrition
                and a visual interpretation of the global unemployment rate.
                """, style={'text-align': 'justify'}
            ),
            html.P(dbc.Button("Learn more", color="primary",
                              href="https://www.analyticsinhr.com/blog/what-is-hr-analytics/"), className="lead"),
        ]
    )

])

body2 = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Unemployment around the World"),
            html.P(
                """\
Global unemployment has fallen to its lowest level in almost 40 years, 
a breakthrough economists attribute to changes including more flexible 
working practices, lower wages and rock-bottom interest rates.
""", style={'text-align': 'justify'}),

            html.P(
                """\
Slightly more than 172 million people globally were unemployed in 2018. 
That is about 2 million less than the previous year. The International
Labor Organization expects the global unemployment rate of five percent 
to remain essentially unchanged over the next few years.
ILO experts also highlight the lack of progress in closing the gender gap 
in labor force participation. They note only 48 percent of women are working,
compared to 75 percent of men.

""", style={'text-align': 'justify'}),

            html.P(
                """\
Another worrying issue is high youth unemployment. 
The ILO says one in five young people under 25 are jobless and have no skills.
It warns this compromises their future employment prospects.

""", style={'text-align': 'justify'}),

            html.Br()
        ],
            md=4,
        ),
        dbc.Col([
            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                     style={'width': '5', 'height': '5', 'display': 'inline-block'}),
            html.Br(),
        ]),



    ])
], className="mt-4")

body3 = dbc.Container([
    dbc.NavbarSimple([
        dbc.Popover(
            [dbc.PopoverHeader("Instruction"),
             dbc.PopoverBody("""Change the slider to know the global state
                                    from the data. 
                                    """)],
            id="popover2",
            is_open=False,
            target="popover-target2"
        ),
    ],
        brand="An Analysis on Unemployment",
        brand_style={'font-weight': 'bold', 'font-size': '30px'}),
    html.Br(),
    dbc.Jumbotron(
        [
            html.H3("The Global Unemployment Rate (1991-2019)",
                    className="display-3"),
            html.P(
                """
                Lower rates of unemployment are generally presented as
                great news, but for employers struggling to fill vacancies, 
                the news is decidedly less wanted. This is because low 
                unemployment means fewer individuals applying for any given j
                ob vacancy—there are simply fewer people looking and therefore
                fewer available to apply. This, in turn, can mean there are 
                fewer people applying who are actually fully qualified for 
                a given role.
                
                """,
                className="lead", style={'text-align': 'justify'}
            ),
            html.P(
                """
                Therefore, it becomes more critical for employers to get
                more qualified applicants and to keep the best-qualified 
                applicants interested and engaged through the recruiting 
                process—and securing a “yes” when an offer is made. With this,
                let us first observe the unemployment rates throughout the
                world for the past few decades.
                """,
                className="lead", style={'text-align': 'justify'}
            ),
            html.Hr(className="my-2"),
            html.P(
                dbc.Button("Click to View Instructions",
                           id="simple-toast-toggle3", color="primary"),
            ),
            dbc.Toast(
                [html.P("""
                Change the slider to know the global state from the data. .
                """)],
                id="simple-toast3",
                header="Instructions",
                icon="primary",
                duration=10000,
                dismissable=True
            )


        ]
    ),



    html.Div([
        dcc.Slider(
            id='Year-Slider1',
            min=1991,
            max=2019,
            marks={i: 'Label {}'.format(i) if i == 1 else str(
                i) for i in range(1991, 2021, 5)},
            value=1991)], style={'display': 'block'}),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Div([
        html.Div(id='Slider-output-container',
                 style={'display': 'block'})
    ]),

    html.Div([
        dcc.Graph(id='map-output-container',
                  style={'display': 'block'})
    ], style={'height': '800px', 'display': 'block'}),


    html.P(
        """
        Based on the global representation of unemployment, it can be observed
        that unemployment rates have decreased over the past few decades. 
        Notable countries whose unemployment rates have decreased from 1991 to
        2019 include Canada, United States, the Philippines and Australia.
        However some countries have their unemployment rates increased and
        some of these countries include Turkey, Brazil and Iran. However,
        analysts have predicted that for the next decade, unemployment rates
        will continue to decrease and that Artificial Intelligence will actually
        aid Humans in their everyday jobs.
        """, style={'text-align': 'justify', 'display': 'block'}),
    html.P(
        """
        We now ask ourselves, what are the causes of unemployment. According
        to HR Analysts, there are actually seven causes of unemployment 
        categorized into 3 main classes: Cyclical, Structural and Frictional.
        Frictional refers to a type of unemployment  when employees leave their 
        job to find a better one. Structural refers to when workers' 
        skills or income requirements no longer match the jobs available.
        Cyclical then refers to the cyclic entry to the workforce. 
        """, style={'text-align': 'justify', 'display': 'block'}),

    html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()),
             style={'width': '20', 'height': '5'}),
    html.Br(),
    html.Br(),
    html.P(
        """
        These are the main causes of unemployment however not all joblessness
        cause unemployment. If someone retires, goes back to school or
        leaves the workforce to take care of children or other family members, 
        that is not unemployment because they no longer look for work. 
        The natural rate of unemployment is between 4.5% and 5% according to
        statisticians.
        In the end unemployment is a key economic indicator. 
        High employment rates can be symptomatic of a distressed economy. 
        Conversely, very low unemployment rates can signal an overheated one.
        """, style={'text-align': 'justify', 'display': 'block'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Hr(),



])

body4 = dbc.Container([
    html.Br(),
    dbc.NavbarSimple([
        dbc.Popover(
            [dbc.PopoverHeader("Instruction"),
             dbc.PopoverBody("""Use the sliders as input values in predicting
                            the job offer acceptance of an employee.
                            """)],
            id="popover7",
            is_open=False,
            target="popover-target7"
        ),
    ],
        brand="Predictive Analytics",
        brand_style={'font-weight': 'bold', 'font-size': '25px'}),
    html.Br(),


    dbc.Jumbotron([
        html.H1("Prediction of an Applicant's Job Offer Acceptance",
                className="display-4"),
        html.P(
            """
                As one of the causes of unemployment (getting picky in jobs),
                it is absolutely helpful in HR management in knowing the rate
                at which shortlisted applicants are actually accepting the
                job offer. In Talent Acquisition, the number of shortlisted 
                applicants actually accepting an offer is an important metric 
                as it can directly affect the cost of Talent Acquisition.
                This metric is known as the "Join Ratio". In addition to 
                higher cost of acquisition, low join ratio may result 
                in direct loss of revenue because of placement delays in 
                important client assignments. For this module, we seek to
                predict if an applicant will either accept or decline a
                job offer. The features given here are determined to be the
                most important factors in an applicant's decision making.
                
                """,
            className="lead", style={'text-align': 'justify'}
        ),
        html.Hr(className="my-2"),
        html.P(
            "This is a predictive analytics tool created using classification\
                 techniques of Machine Learning"
        ),
        html.P(
            dbc.Button("Click to View Instructions",
                       id="simple-toast-toggle", color="primary"),
        ),
        dbc.Toast(
            [html.P("""
                The given features are chosen since they are the factors
                that were observed to be significant in assessing the
                applicant's job offer acceptance process.
                
                """)],
            id="simple-toast",
            header="Instructions",
            icon="primary",
            duration=10000,
            dismissable=True
        )
    ]),

    dbc.Row([
        dbc.Col([
            html.Div('Cost-Related', style={'font-weight': 'bold',
                                            'font-size': '30px',
                                            'display': 'inline-block'}),


            html.Br(),
            html.Br(),
            html.Div([
                html.Label("""What is the total amount the management plans to pay\
                        to the hired candidate? (Choose 0 if not yet defined)""",
                           style={'fontWeight': 'bold',
                                  'fontSize': 17}),
                dcc.Slider(
                    id='Value',
                    min=0,
                    max=100000,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(
                        i) for i in range(0, 100000, 10000)},
                    value=0)]),

            html.Br(),
            html.Br(),
            html.Div([
                html.Div(id='Prediction-slider-output1')
            ], style={'display': 'inline-block'}),


            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                html.Label("""What is the requested salary amount of the 
                            candidate? (Choose 0 when unspecified 
                            and for negotiation)""",
                           style={'fontWeight': 'bold',
                                  'fontSize': 17}),
                dcc.Slider(
                    id='Value3',
                    min=0,
                    max=60000,
                    step=0.1,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(
                        i) for i in range(0, 60005, 10000)},
                    value=0)]),

            html.Br(),
            html.Br(),
            html.Div([
                html.Div(id='Prediction-slider-output3')
            ], style={'display': 'inline-block'}),

        ]),



        dbc.Col([
            html.Br(),
            html.Br(),
            html.Div([
                html.Label("""What is the net cost in hiring the candidate 
                including the taxes? (Choose a negative value when
                amount to pay the candidate has not yet
                been defined and is still open for negotiation)""",
                           style={'fontWeight': 'bold',
                                  'fontSize': 17}),
                dcc.Slider(
                    id='Value4',
                    min=-10000,
                    max=30000,
                    step=1,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(
                        i) for i in range(-10005, 30005, 5000)},
                    value=0)]),

            html.Br(),
            html.Br(),
            html.Div([
                html.Div(id='Prediction-slider-output4')
            ], style={'display': 'inline-block'}),


        ]),

    ]),

    dbc.Row([
        dbc.Col([
            html.Br(style={'borderWidth': '10px'}),

            html.Br(),
            html.Hr(),
            html.Div('Process-Related', style={'font-weight': 'bold',
                                               'font-size': '30px',
                                               'display': 'inline-block'}),

            html.Br(),
            html.Br(),
            html.Div([
                html.Label("""How many days was the position closed?
                """,
                           style={'fontWeight': 'bold',
                                  'fontSize': 17}),
                dcc.Slider(
                    id='Value11',
                    min=0,
                    max=200,
                    step=1,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(
                        i) for i in range(0, 201, 50)},
                    value=0)]),

            html.Br(),
            html.Br(),
            html.Div([
                html.Div(id='Prediction-slider-output11')
            ], style={'display': 'inline-block'}),


            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                html.Label("""How many days did the entire recruitment process
                take?
                """,
                           style={'fontWeight': 'bold',
                                  'fontSize': 17}),
                dcc.Slider(
                    id='Value13',
                    min=0,
                    max=200,
                    step=1,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(
                        i) for i in range(0, 201, 50)},
                    value=0)]),

            html.Br(),
            html.Br(),
            html.Div([
                html.Div(id='Prediction-slider-output13')
            ], style={'display': 'inline-block'}),


        ]),


        dbc.Col([
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                html.Label("""How many days was the job offer approved?
                """,
                           style={'fontWeight': 'bold',
                                  'fontSize': 17}),
                dcc.Slider(
                    id='Value12',
                    min=0,
                    max=200,
                    step=1,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(
                       i) for i in range(0, 201, 50)},
                    value=0)]),

            html.Br(),
            html.Br(),
            html.Div([
                html.Div(id='Prediction-slider-output12')
            ], style={'display': 'inline-block'}),


        ])

    ]),

    html.Br(),
    dbc.Row([
        html.Br(),
        html.Br(),
        html.H2(id='Prediction-output1', style={'margin': '20px',
                                                'display': 'inline-block',
                                                'fontWeight': 'bold',
                                                'fontSize': 24,
                                                'border-radius': '10px',
                                                'padding': '10px 10px 10px 10px',
                                                'background-color': '#D3D3D3'}),
    ]),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Hr(),
])


body5 = dbc.Container([
    html.Br(),
    dbc.NavbarSimple([
        dbc.Popover(
            [dbc.PopoverHeader("Instruction"),
             dbc.PopoverBody("""Use the sliders as input values in predicting
                            the job offer acceptance of an employee.
                            """)],
            id="popover8",
            is_open=False,
            target="popover-target8"
        ),
    ],
        brand="Predictive Analytics",
        brand_style={'font-weight': 'bold', 'font-size': '25px'}),
    html.Br(),

    dbc.Jumbotron([
        html.H1("Prediction of Employee Attrition",
                className="display-4"),
        html.P(
            """
                Attrition in human resources refers to the gradual loss
                of employees over time. In general, relatively high attrition
                is problematic for companies. HR professionals often assume a
                leadership role in designing company compensation programs,
                work culture and motivation systems that help the organization
                retain top employees.
                A major problem in high employee attrition is its cost to an 
                organization. Job postings, hiring processes, paperwork and 
                new hire training are some of the common expenses of losing 
                employees and replacing them. Additionally, regular employee 
                turnover prohibits your organization from increasing its 
                collective knowledge base and experience over time. 
                This is especially concerning if your business is customer
                facing, as customers often prefer to interact with familiar 
                people. Errors and issues are more likely if you constantly 
                have new workers.
                """,
            className="lead", style={'text-align': 'justify'}
        ),
        html.P(
            """
                With advances in machine learning and data science, 
                its possible to not only predict employee attrition
                but to understand the key variables that influence turnover.
                For this module, the goal is to predict employee attrition 
                using the relevant features of the data. This predictive 
                capability is useful for Talent acquisition management 
                for predicting turnover is at the forefront of needs of
                Human Resources (HR) in many organizations. 
                """,
            className="lead", style={'text-align': 'justify'}
        ),
        html.Hr(className="my-2"),
        html.P(
            "This is a predictive analytics tool created using classification\
                 techniques of Machine Learning"
        ),
        html.P(
            dbc.Button("Click to View Instructions",
                       id="simple-toast-toggle2", color="primary"),
        ),
        dbc.Toast(
            [html.P("""
                The given features are chosen since they are the factors
                that were observed to be significant in predicting employee
                attrition.
                
                """)],
            id="simple-toast2",
            header="Instructions",
            icon="primary",
            duration=10000,
            dismissable=True
        )
    ]),

    dbc.Row([
        dbc.Col([
            html.Br(),
            html.Br(),
            html.Div([
                html.Label("""
                1.) Pls. specify the age of the employee
                """,
                           style={'fontWeight': 'bold',
                                  'fontSize': 24}),
                dcc.Slider(
                    id='age',
                    min=18,
                    max=80,
                    step=1,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(
                        i) for i in range(18, 81, 2)},
                    value=0)]),

            html.Br(),
            html.Br(),
            html.Div([
                html.Div(id='Prediction-slider-output14')
            ], style={'display': 'inline-block'}),



            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                html.Label("""
                2.) Pls. specify the estimated monthly income of the employee
                """,
                           style={'fontWeight': 'bold',
                                  'fontSize': 24}),
                dcc.Slider(
                    id='monthly',
                    min=1000,
                    max=25000,
                    step=100,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(
                        i) for i in range(1000, 25001, 1000)},
                    value=0)]),

            html.Br(),
            html.Br(),
            html.Div([
                html.Div(id='Prediction-slider-output15')
            ], style={'display': 'inline-block'}),



            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                html.Label("""
                3.) Pls. specify how many years the employee stayed with the 
                current company
                """,
                           style={'fontWeight': 'bold',
                                  'fontSize': 24}),
                dcc.Slider(
                    id='stay',
                    min=0,
                    max=40,
                    step=1,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(
                        i) for i in range(0, 41, 5)},
                    value=0)]),

            html.Br(),
            html.Br(),
            html.Div([
                html.Div(id='Prediction-slider-output16')
            ], style={'display': 'inline-block'}),



            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                html.Label("""
                4.) Pls. specify how many years the employee was last 
                promoted
                """,
                           style={'fontWeight': 'bold',
                                  'fontSize': 24}),
                dcc.Slider(
                    id='promote',
                    min=0,
                    max=20,
                    step=1,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(
                        i) for i in range(0, 21, 5)},
                    value=0)]),

            html.Br(),
            html.Br(),
            html.Div([
                html.Div(id='Prediction-slider-output17')
            ], style={'display': 'inline-block'}),



            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                html.Label("""
                5.) Pls. specify the total number of years the employee
                has worked as a professional
                """,
                           style={'fontWeight': 'bold',
                                  'fontSize': 24}),
                dcc.Slider(
                    id='total',
                    min=0,
                    max=40,
                    step=1,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(
                        i) for i in range(0, 41, 5)},
                    value=0)]),

            html.Br(),
            html.Br(),
            html.Div([
                html.Div(id='Prediction-slider-output18')
            ], style={'display': 'inline-block'}),



            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                html.Label("""
                6.) Pls. rate the company's work-life-balance (1 is the lowest
                and 4 being the highest rating)
                """,
                           style={'fontWeight': 'bold',
                                  'fontSize': 24}),
                dcc.Slider(
                    id='balance',
                    min=1,
                    max=4,
                    step=1,
                    marks={i: 'Label {}'.format(i) if i == 0.5 else str(
                        i) for i in range(1, 5, 1)},
                    value=0)]),

            html.Br(),
            html.Br(),
            html.Div([
                html.Div(id='Prediction-slider-output19')
            ], style={'display': 'inline-block'}),




            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                html.Label("""
                7.) Pls. rate the company's working environment (1 is the lowest
                and 4 being the highest rating)
                """,
                           style={'fontWeight': 'bold',
                                  'fontSize': 24}),
                dcc.Slider(
                    id='environment',
                    min=1,
                    max=4,
                    step=1,
                    marks={i: 'Label {}'.format(i) if i == 0.5 else str(
                        i) for i in range(1, 5, 1)},
                    value=0)]),

            html.Br(),
            html.Br(),
            html.Div([
                html.Div(id='Prediction-slider-output20')
            ], style={'display': 'inline-block'}),




            html.Br(),
            dbc.Row([
                html.Br(),
                html.Br(),
                html.H2(id='Prediction-output2', style={'margin': '20px',
                                                        'display': 'inline-block',
                                                        'fontWeight': 'bold',
                                                        'fontSize': 24,
                                                        'border-radius': '10px',
                                                        'padding': '10px 10px 10px 10px',
                                                        'background-color': '#D3D3D3'}),
            ]),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Hr(),


        ])
    ])
])


body6 = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.H2("Dustin Reyes"),
            html.P(
                """\
        Dustin is a student of the Master of Science in Data Science program 
        of the Asian Institute of Management. He graduated in De La Salle 
        University with a bachelor's degree in Electronics and Communications
        Engineering. Prior to his graduate studies, he worked as a Product
        Analysis Engineer from Analog Devices, Inc. and it from there that
        he was exposed to Data Science and its potentials. 
        """, style={'text-align': 'justify'}),

            html.P(
                """\
        The Asian Institute of Management’s Master of Science in Data Science 
        (MSDS) is a pioneering program designed from the practitioner’s point 
        of view. Moreover, learning will directly address one particular pain 
        point of the enterprise — when its data scientists cannot provide 
        unique actionable insights.

        At AIM, data scientists work closely with domain experts familiar 
        with business and management issues. Students will, therefore, learn 
        how to formulate the right questions and identify the correct d
        atasets to address highly diverse business and research problems. 
        """, style={'text-align': 'justify'}),

            html.Br()
        ],
            md=4,
        ),
        dbc.Col([
            html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()),
                     style={'width': '50%', 'height': '100%', 'display': 'inline-block'}),
            html.Br(),
        ]),
    ]),

    dbc.Row([
        dbc.Col([
            html.Br(),
            html.Br(),
            html.H2("References and Acknowledgements"),
            html.P(
                """\
        In creating this project, the author would like to thank
        Professor Eduardo David Jr. for his teachings about Data Applications,
        Professor Christopher Monterola and Professor Erika Legara for
        their teachings on Machine Learning and Data Visualization.
        
        """, style={'text-align': 'justify'}),
        ])
    ]),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Hr(),


])


# --------------------Tab Arrangement-------------------------------------------

tab1_content = dbc.Card(
    dbc.CardBody([navbar, body, body2, body3])
)

tab2_content = dbc.Card(
    dbc.CardBody([navbar, body4])
)

tab3_content = dbc.Card(
    dbc.CardBody([navbar, body5])
)

tab4_content = dbc.Card(
    dbc.CardBody([navbar, body6])
)

tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Introduction"),
        dbc.Tab(tab2_content, label="Prediction of Employee Job Offer Acceptance"),
        dbc.Tab(tab3_content, label="Prediction of Employee Attrition"),
        dbc.Tab(tab4_content, label="About the author"),
    ]
)


# -----------------------------Application Layout-----------------------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])
# app.config.suppress_callback_exceptions = True
app.layout = html.Div([tabs])


# -------------------------------CALLBACKS------------------------------------

# PAGE 1 CALLBACKS
@app.callback(
    Output("simple-toast3", "is_open"),
    [Input("simple-toast-toggle3", "n_clicks")],
)
def open_toast3(n):
    return True


@app.callback(
    Output('Slider-output-container', 'children'),
    [Input('Year-Slider1', 'value')])
def update_output1(year):
    return 'The Global Unemployment Rate for the Year {}'.format(year)


@app.callback(
    Output('map-output-container', 'figure'),
    [Input('Year-Slider1', 'value')])
def update_output2(year):
    trace = go.Choropleth(locations=df_unemployment['Country Code'],
                          z=df_unemployment['{}'.format(year)],
                          text=df_unemployment['Country Name'],
                          autocolorscale=False,
                          colorscale="reds",
                          marker={
                              'line': {'color': 'rgb(180,180,180)', 'width': 0.5}},
                          colorbar={"thickness": 10, "len": 0.3, "x": 0, "y": 0.5})
    return {"data": [trace],
            "layout": go.Layout(
        margin=dict(
            b=60,
            t=50),
        height=800, width=1100, geo={'showframe': True, 'showcoastlines': True,
                                     'projection': {'type': "miller"}})}


# PAGE 2 CALLBACKS

@app.callback(
    Output("simple-toast", "is_open"),
    [Input("simple-toast-toggle", "n_clicks")],
)
def open_toast(n):
    return True


# Sliders for Page2
@app.callback(
    Output('Prediction-slider-output1', 'children'),
    [Input('Value', 'value')])
def prediction_outputslider1(val1):
    return f'The employer is willing to pay an amount of : ${val1}'


@app.callback(
    Output('Prediction-slider-output3', 'children'),
    [Input('Value3', 'value')])
def prediction_outputslider3(val3):
    return f'The candidate asked for a salary amount of : ${val3}'


@app.callback(
    Output('Prediction-slider-output4', 'children'),
    [Input('Value4', 'value')])
def prediction_outputslider4(val4):
    return f'The netcost of hiring the candidate is : ${val4}'


@app.callback(
    Output('Prediction-slider-output11', 'children'),
    [Input('Value11', 'value')])
def prediction_outputslider11(val11):
    return f'The position was closed in: {val11} days'


@app.callback(
    Output('Prediction-slider-output12', 'children'),
    [Input('Value12', 'value')])
def prediction_outputslider12(val12):
    return f'The number of days the job offer was approved: {val12} days'


@app.callback(
    Output('Prediction-slider-output13', 'children'),
    [Input('Value13', 'value')])
def prediction_outputslider13(val13):
    return f'The entire recruitment process took: {val13} days'


# Prediction Callback for Page 2
@app.callback(
    Output('Prediction-output1', 'children'),
    [Input('Value', 'value'),
     Input('Value3', 'value'),
     Input('Value4', 'value'),
     Input('Value11', 'value'),
     Input('Value12', 'value'),
     Input('Value13', 'value')])
def predict(Value, Value3, Value4, Value11, Value12, Value13):
    df = pd.DataFrame(
        columns=['Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6'],
        data=[[Value11, Value12, Value13, Value4, Value, Value3]])

    fname = 'data/model5_acceptance.pkl'
    model = joblib.load(open(fname, 'rb'))
    y_pred = model.predict(df)
    if y_pred[0] == 1:
        res = 'the applicant is likely to DECLINE the offer'
    else:
        res = 'the applicant would NOT DECLINE the offer'
    result = f'The predicted outcome is {res}'
    return result


# PAGE 3 CALLBACKS
@app.callback(
    Output("simple-toast2", "is_open"),
    [Input("simple-toast-toggle2", "n_clicks")],
)
def open_toast2(n):
    return True


@app.callback(
    Output('Prediction-slider-output14', 'children'),
    [Input('age', 'value')])
def prediction_outputslider14(val14):
    return f'The age of the employee of choice is: {val14} yrs old'


@app.callback(
    Output('Prediction-slider-output15', 'children'),
    [Input('monthly', 'value')])
def prediction_outputslider15(val15):
    return f'The estimated monthly income of the employee of choice is: ${val15}'


@app.callback(
    Output('Prediction-slider-output16', 'children'),
    [Input('stay', 'value')])
def prediction_outputslider16(val16):
    return f'The employee have stayed with the company by: {val16} years'


@app.callback(
    Output('Prediction-slider-output17', 'children'),
    [Input('promote', 'value')])
def prediction_outputslider17(val17):
    return f'The number of years the employee was last promoted was: {val17} years'


@app.callback(
    Output('Prediction-slider-output18', 'children'),
    [Input('total', 'value')])
def prediction_outputslider18(val18):
    return f'The number of years the employee has been working is: {val18} years'


@app.callback(
    Output('Prediction-slider-output19', 'children'),
    [Input('balance', 'value')])
def prediction_outputslider19(val19):
    return f'The rating that you have given for the company work-life-balance is: {val19}'


@app.callback(
    Output('Prediction-slider-output20', 'children'),
    [Input('environment', 'value')])
def prediction_outputslider20(val20):
    return f'The rating that you have given for the company working environment is: {val20}'

# Prediction Callback for Page 3


@app.callback(
    Output('Prediction-output2', 'children'),
    [Input('age', 'value'),
     Input('monthly', 'value'),
     Input('stay', 'value'),
     Input('promote', 'value'),
     Input('total', 'value'),
     Input('balance', 'value'),
     Input('environment', 'value')])
def predict2(age, monthly, stay, promote, total, balance, environment):
    df = pd.DataFrame(
        columns=['Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7'],
        data=[[age, monthly, stay, promote, total, balance, environment]])

    fname = 'data/model2.pkl'
    model = joblib.load(open(fname, 'rb'))
    y_pred = model.predict(df)
    if y_pred[0] == 1:
        res = 'the applicant is likely for attrition'
    else:
        res = 'the applicant is not likely for attrition'
    result = f'The predicted outcome is {res}'
    return result


if __name__ == '__main__':
    app.run_server(debug=False, port=8082)


# In[ ]:




