from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    company_data = {
        'name': 'STRATEGICSHIFT CONSULTING',
        'tagline': 'Strategic Partnerships for Transformative Growth',
        'subtagline': 'Driving Operational Excellence, Maximizing Your Potential', 
        'enterprise_number': '2025/451935/07',
        
        'hero_title': 'Enterprise Transformation<br>Redefined',
        'hero_subtitle': 'Where Strategic Vision Meets Execution Excellence',
        
        'intro': 'In an era of unprecedented complexity, exceptional organizations require exceptional partnerships. We deliver the strategic clarity, operational precision, and digital innovation that separates market leaders from followers.',
        
        'vision': 'To architect the future of African enterprise through strategic innovation, operational mastery, and transformative digital solutions.',
        
        'mission': 'To equip visionary leaders with the strategic frameworks, operational systems, and digital capabilities needed to dominate their markets and define their industries.',
        
        'value_props': [
            {'icon': 'chess-queen', 'title': 'Strategic Mastery', 'desc': 'Board-level advisory with ground-level execution'},
            {'icon': 'rocket', 'title': 'Transformative Results', 'desc': 'Measurable ROI and sustainable competitive advantage'},
            {'icon': 'shield-alt', 'title': 'Enterprise Security', 'desc': 'Risk-mitigated, compliance-guaranteed operations'},
            {'icon': 'brain', 'title': 'Innovation Engine', 'desc': 'Future-proof strategies with cutting-edge technology'}
        ],
        
        'services': [
            {
                'category': 'Strategic Advisory',
                'icon': 'chess-queen',
                'color': 'accent',
                'capabilities': [
                    'Corporate Strategy & Market Positioning',
                    'Digital Transformation Roadmapping', 
                    'M&A Strategy & Integration',
                    'Executive Leadership Development',
                    'Innovation Ecosystem Development'
                ],
                'description': 'Board-level strategic guidance with actionable implementation frameworks'
            },
            {
                'category': 'Digital Excellence',
                'icon': 'code',
                'color': 'primary', 
                'capabilities': [
                    'Enterprise Web Architecture',
                    'Digital Product Strategy & Development',
                    'AI & Machine Learning Integration',
                    'Cloud Infrastructure Design',
                    'Cyber Security Fortification'
                ],
                'description': 'Future-proof digital solutions that drive competitive advantage'
            },
            {
                'category': 'Operational Mastery',
                'icon': 'cogs',
                'color': 'secondary',
                'capabilities': [
                    'Process Optimization & Automation',
                    'Supply Chain Transformation',
                    'Vendor Management Ecosystems',
                    'Operational Risk Management',
                    'Performance Excellence Frameworks'
                ],
                'description': 'End-to-end operational transformation for peak efficiency'
            },
            {
                'category': 'TFA Transportation',
                'icon': 'bus',
                'color': 'gold',
                'capabilities': [
                    '24/7 Enterprise Staff Logistics',
                    'Fleet Management & Optimization',
                    'Route Intelligence & Analytics',
                    'Employee Experience Enhancement',
                    'Sustainability Integration'
                ],
                'description': 'Seamless, reliable transportation solutions for enterprise workforce'
            },
            {
                'category': 'Property Excellence',
                'icon': 'building',
                'color': 'teal',
                'capabilities': [
                    'Property Portfolio Management',
                    'Rental & Sales Acquisition Services',
                    'Bond Origination & Advisory',
                    'Investment & Market Analysis',
                    'Tenant Relationship Management'
                ],
                'description': 'End-to-end property solutions and strategic financial guidance'
            },
            {
                'category': 'Corporate Environments',
                'icon': 'broom',
                'color': 'green',
                'capabilities': [
                    'Customized Corporate Cleaning Plans',
                    'Deep Cleaning & Sanitization',
                    'Green & Sustainable Cleaning',
                    'Specialized Surface & Floor Care',
                    'Vetted & Uniformed Staff'
                ],
                'description': 'Professional in-house cleaning for health, safety, and brand image'
            }
        ],
        
        'case_studies': [
            {'metric': '214%', 'description': 'Revenue Growth for FinTech Client'},
            {'metric': '63%', 'description': 'Operational Efficiency Improvement'},
            {'metric': '₿4.2M', 'description': 'Cost Savings Delivered'},
            {'metric': '100%', 'description': 'Client Retention Rate'}
        ],
        
        'principles': [
            {'icon': 'gem', 'title': 'Excellence', 'description': 'We deliver beyond expectations, setting new standards in every engagement.'},
            {'icon': 'handshake', 'title': 'Partnership', 'description': 'Your success is our success. We invest deeply in your journey.'},
            {'icon': 'lightbulb', 'title': 'Innovation', 'description': 'We challenge conventions and pioneer new approaches to complex problems.'},
            {'icon': 'shield', 'title': 'Integrity', 'description': 'Uncompromising ethics and transparent communication guide every decision.'}
        ],
        
        'process': [
            {'step': '01', 'title': 'Discovery & Diagnostic', 'description': 'Deep immersion into your challenges, opportunities, and ambitions'},
            {'step': '02', 'title': 'Strategy Architecture', 'description': 'Custom-crafted solutions aligned with your vision and market reality'},
            {'step': '03', 'title': 'Precision Execution', 'description': 'Flawless implementation with continuous optimization and adaptation'},
            {'step': '04', 'title': 'Growth Acceleration', 'description': 'Sustained partnership driving continuous improvement and expansion'}
        ],
        
        'leadership_quotes': [
            {'quote': 'StrategicShift transformed our operational DNA. The results speak for themselves.', 'author': 'CEO, Financial Services'},
            {'quote': 'Their digital expertise gave us a 3-year competitive advantage in 6 months.', 'author': 'CTO, Technology Firm'},
            {'quote': 'More than consultants—true strategic partners invested in our success.', 'author': 'Board Chair, Manufacturing'}
        ],
        
        'contact': {
            'phones': ['+27 68 852 7197', '+27 69 679 3558'],
            'email': 'StrategicShift.Consulting@outlook.com',
            'address': 'South Africa • Global Business Hubs • Emerging Markets'
        }
    }
    return render_template('index.html', company=company_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
