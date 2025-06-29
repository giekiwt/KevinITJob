from django.core.management.base import BaseCommand
from blog_posts.models import BlogPost
from django.utils import timezone

class Command(BaseCommand):
    help = 'Import 20 real blog data with actual IT content (without deleting existing)'

    def handle(self, *args, **kwargs):
        # Không xóa dữ liệu cũ, chỉ thêm mới
        existing_count = BlogPost.objects.count()
        
        blog_data = [
            {
                'title': 'Làm thế nào để trở thành một Full-Stack Developer trong 6 tháng',
                'summary': 'Hướng dẫn chi tiết lộ trình học tập và thực hành để trở thành Full-Stack Developer từ con số 0.',
                'content': '<h2>Giới thiệu</h2><p>Trở thành một Full-Stack Developer là mục tiêu của nhiều người trong ngành IT. Bài viết này sẽ chia sẻ lộ trình học tập chi tiết trong 6 tháng.</p><h2>Tháng 1-2: Nền tảng cơ bản</h2><ul><li>HTML, CSS cơ bản và nâng cao</li><li>JavaScript ES6+ và DOM manipulation</li><li>Git và GitHub</li><li>Responsive design</li></ul><h2>Tháng 3-4: Backend Development</h2><ul><li>Python và Django Framework</li><li>Database design và SQL</li><li>RESTful APIs</li><li>Authentication và Authorization</li></ul><h2>Tháng 5-6: Frontend Framework và Deployment</h2><ul><li>React.js hoặc Vue.js</li><li>State management (Redux/Vuex)</li><li>Docker và containerization</li><li>Deployment lên cloud (AWS, Heroku)</li></ul>',
                'tags': 'Full-Stack, JavaScript, Python, Django, React, Lập trình',
                'image': 'blog_images/fullstack.jpg',
            },
            {
                'title': 'Top 10 kỹ năng cần thiết cho Developer năm 2024',
                'summary': 'Những kỹ năng quan trọng nhất mà mọi developer cần có để thành công trong ngành IT hiện đại.',
                'content': '<h2>1. Cloud Computing</h2><p>Kiến thức về AWS, Azure, hoặc Google Cloud Platform là bắt buộc trong thời đại cloud-first.</p><h2>2. DevOps và CI/CD</h2><p>Docker, Kubernetes, Jenkins giúp tự động hóa quy trình phát triển và triển khai.</p><h2>3. Machine Learning cơ bản</h2><p>Hiểu biết về ML và AI sẽ mở ra nhiều cơ hội mới trong ngành.</p><h2>4. Cybersecurity</h2><p>Bảo mật ứng dụng và dữ liệu người dùng là ưu tiên hàng đầu.</p><h2>5. Mobile Development</h2><p>React Native, Flutter giúp phát triển ứng dụng đa nền tảng.</p>',
                'tags': 'Kỹ năng, Developer, Cloud, DevOps, AI, Bảo mật',
                'image': 'blog_images/skills2024.jpg',
            },
            {
                'title': 'Hướng dẫn phỏng vấn Frontend Developer: Từ cơ bản đến nâng cao',
                'summary': 'Chuẩn bị kỹ lưỡng cho buổi phỏng vấn Frontend Developer với các câu hỏi thường gặp và tips hữu ích.',
                'content': '<h2>Chuẩn bị trước phỏng vấn</h2><p>Nghiên cứu kỹ về công ty, sản phẩm, và công nghệ họ đang sử dụng.</p><h2>Câu hỏi cơ bản</h2><h3>HTML/CSS</h3><ul><li>Semantic HTML là gì?</li><li>CSS Grid vs Flexbox</li><li>Responsive design principles</li><li>CSS preprocessors (Sass, Less)</li></ul><h3>JavaScript</h3><ul><li>Closures và scope</li><li>Promises và async/await</li><li>Event delegation</li><li>ES6+ features</li></ul><h2>Câu hỏi nâng cao</h2><ul><li>Performance optimization</li><li>Browser rendering process</li><li>Cross-browser compatibility</li><li>Accessibility (a11y)</li></ul>',
                'tags': 'Phỏng vấn, Frontend, JavaScript, HTML, CSS, Career',
                'image': 'blog_images/frontend_interview.jpg',
            },
            {
                'title': 'Docker cho Beginners: Container hóa ứng dụng từ A đến Z',
                'summary': 'Học Docker từ cơ bản đến nâng cao, từ khái niệm container đến deployment production.',
                'content': '<h2>Docker là gì?</h2><p>Docker là platform để phát triển, ship, và chạy ứng dụng trong containers. Containers là lightweight, portable, và self-sufficient.</p><h2>Cài đặt Docker</h2><p>Hướng dẫn cài đặt Docker Desktop trên Windows, macOS, và Linux.</p><h2>Docker Basics</h2><h3>Dockerfile</h3><p>Tạo file Dockerfile để build image:</p><pre><code>FROM node:16\nWORKDIR /app\nCOPY package*.json ./\nRUN npm install\nCOPY . .\nEXPOSE 3000\nCMD ["npm", "start"]</code></pre><h3>Docker Commands</h3><ul><li>docker build -t myapp .</li><li>docker run -p 3000:3000 myapp</li><li>docker ps</li><li>docker images</li></ul>',
                'tags': 'Docker, Container, DevOps, Deployment, Cloud',
                'image': 'blog_images/docker.jpg',
            },
            {
                'title': 'React Hooks: Từ useState đến Custom Hooks',
                'summary': 'Khám phá sức mạnh của React Hooks và cách sử dụng chúng hiệu quả trong ứng dụng React.',
                'content': '<h2>React Hooks là gì?</h2><p>Hooks cho phép bạn sử dụng state và lifecycle methods trong functional components.</p><h2>useState Hook</h2><p>useState là hook cơ bản nhất để quản lý state trong functional components:</p><pre><code>import React, { useState } from \'react\';\n\nfunction Counter() {\n  const [count, setCount] = useState(0);\n  \n  return (\n    <div>\n      <p>Count: {count}</p>\n      <button onClick={() => setCount(count + 1)}>\n        Increment\n      </button>\n    </div>\n  );\n}</code></pre><h2>useEffect Hook</h2><p>useEffect để thực hiện side effects:</p><pre><code>useEffect(() => {\n  // Side effect code\n  return () => {\n    // Cleanup code\n  };\n}, [dependencies]);</code></pre>',
                'tags': 'React, Hooks, JavaScript, Frontend, useState, useEffect',
                'image': 'blog_images/react_hooks.jpg',
            },
            {
                'title': 'Python Django: Xây dựng REST API hoàn chỉnh',
                'summary': 'Hướng dẫn chi tiết cách tạo REST API với Django REST Framework từ setup đến deployment.',
                'content': '<h2>Setup Project</h2><pre><code>pip install django djangorestframework\ndjango-admin startproject api_project\ncd api_project\npython manage.py startapp api</code></pre><h2>Models</h2><pre><code>from django.db import models\n\nclass Article(models.Model):\n    title = models.CharField(max_length=200)\n    content = models.TextField()\n    author = models.ForeignKey(User, on_delete=models.CASCADE)\n    created_at = models.DateTimeField(auto_now_add=True)\n    \n    def __str__(self):\n        return self.title</code></pre><h2>Serializers</h2><pre><code>from rest_framework import serializers\nfrom .models import Article\n\nclass ArticleSerializer(serializers.ModelSerializer):\n    class Meta:\n        model = Article\n        fields = \'__all__\'</code></pre>',
                'tags': 'Django, Python, REST API, DRF, Backend',
                'image': 'blog_images/django_rest.jpg',
            },
            {
                'title': 'Git Workflow: Từ Git Flow đến GitHub Flow',
                'summary': 'Tìm hiểu các workflow phổ biến trong Git và cách áp dụng chúng trong dự án thực tế.',
                'content': '<h2>Git Flow</h2><p>Workflow phức tạp phù hợp cho dự án lớn với nhiều phiên bản.</p><h3>Branches chính:</h3><ul><li><strong>main/master:</strong> Production code</li><li><strong>develop:</strong> Development branch</li><li><strong>feature/*:</strong> New features</li><li><strong>release/*:</strong> Prepare releases</li><li><strong>hotfix/*:</strong> Emergency fixes</li></ul><h2>GitHub Flow</h2><p>Workflow đơn giản hơn, phù hợp cho continuous deployment.</p><h3>Quy trình:</h3><ol><li>Create feature branch từ main</li><li>Make changes và commit</li><li>Push branch lên GitHub</li><li>Create Pull Request</li><li>Review và merge</li><li>Deploy immediately</li></ol>',
                'tags': 'Git, Version Control, Workflow, GitHub, DevOps',
                'image': 'blog_images/git_workflow.jpg',
            },
            {
                'title': 'Database Design: Từ ERD đến Normalization',
                'summary': 'Học cách thiết kế database hiệu quả từ Entity Relationship Diagram đến các dạng chuẩn hóa.',
                'content': '<h2>Entity Relationship Diagram (ERD)</h2><p>ERD là công cụ trực quan để thiết kế database structure.</p><h3>Components:</h3><ul><li><strong>Entities:</strong> Tables (Users, Products, Orders)</li><li><strong>Attributes:</strong> Columns (id, name, email)</li><li><strong>Relationships:</strong> Foreign keys</li></ul><h2>Database Normalization</h2><h3>First Normal Form (1NF)</h3><ul><li>Mỗi cell chứa atomic values</li><li>Không có repeating groups</li><li>Primary key xác định</li></ul><h3>Second Normal Form (2NF)</h3><ul><li>Đạt 1NF</li><li>Không có partial dependencies</li></ul><h3>Third Normal Form (3NF)</h3><ul><li>Đạt 2NF</li><li>Không có transitive dependencies</li></ul>',
                'tags': 'Database, SQL, ERD, Normalization, Design',
                'image': 'blog_images/database_design.jpg',
            },
            {
                'title': 'Microservices Architecture: Thiết kế hệ thống phân tán',
                'summary': 'Tìm hiểu về microservices architecture và cách implement trong dự án thực tế.',
                'content': '<h2>Microservices là gì?</h2><p>Architecture pattern chia ứng dụng thành các services nhỏ, độc lập, có thể deploy riêng biệt.</p><h2>Ưu điểm</h2><ul><li>Scalability: Scale từng service độc lập</li><li>Technology diversity: Mỗi service có thể dùng tech stack khác</li><li>Fault isolation: Lỗi không ảnh hưởng toàn bộ hệ thống</li><li>Team autonomy: Mỗi team quản lý service riêng</li></ul><h2>Nhược điểm</h2><ul><li>Complexity: Quản lý nhiều services</li><li>Network latency: Communication giữa services</li><li>Data consistency: Distributed data management</li><li>Testing complexity: Integration testing khó khăn</li></ul>',
                'tags': 'Microservices, Architecture, Distributed Systems, DevOps',
                'image': 'blog_images/microservices.jpg',
            },
            {
                'title': 'Machine Learning cho Developers: Bắt đầu với Python',
                'summary': 'Hướng dẫn cơ bản về Machine Learning cho developers, từ lý thuyết đến implementation.',
                'content': '<h2>Machine Learning là gì?</h2><p>ML là subset của AI, cho phép máy tính học từ data mà không cần được lập trình rõ ràng.</p><h2>Types of Machine Learning</h2><h3>Supervised Learning</h3><ul><li>Classification: Phân loại email spam/không spam</li><li>Regression: Dự đoán giá nhà</li></ul><h3>Unsupervised Learning</h3><ul><li>Clustering: Phân nhóm khách hàng</li><li>Dimensionality Reduction: Giảm chiều dữ liệu</li></ul><h2>Python Libraries</h2><pre><code># Core ML libraries\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n\n# ML frameworks\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import mean_squared_error</code></pre>',
                'tags': 'Machine Learning, Python, AI, Data Science, TensorFlow',
                'image': 'blog_images/machine_learning.jpg',
            },
            {
                'title': 'JavaScript ES6+: Những tính năng mới bạn cần biết',
                'summary': 'Khám phá các tính năng mới trong ES6+ và cách sử dụng chúng hiệu quả trong dự án.',
                'content': '<h2>Arrow Functions</h2><p>Arrow functions cung cấp cú pháp ngắn gọn hơn:</p><pre><code>// Traditional function\nfunction add(a, b) {\n    return a + b;\n}\n\n// Arrow function\nconst add = (a, b) => a + b;</code></pre><h2>Destructuring</h2><p>Destructuring cho phép trích xuất dữ liệu từ arrays và objects:</p><pre><code>// Array destructuring\nconst [first, second, ...rest] = [1, 2, 3, 4, 5];\n\n// Object destructuring\nconst { name, age, ...otherProps } = user;</code></pre><h2>Template Literals</h2><p>Template literals cho phép nhúng biểu thức trong chuỗi:</p><pre><code>const name = "John";\nconst greeting = `Hello, ${name}!`;</code></pre>',
                'tags': 'JavaScript, ES6, Modern JavaScript, Frontend',
                'image': 'blog_images/js_es6.jpg',
            },
            {
                'title': 'Node.js và Express: Xây dựng RESTful API',
                'summary': 'Hướng dẫn tạo RESTful API với Node.js và Express framework.',
                'content': '<h2>Setup Project</h2><pre><code>npm init -y\nnpm install express cors dotenv</code></pre><h2>Basic Server</h2><pre><code>const express = require(\'express\');\nconst cors = require(\'cors\');\nconst app = express();\n\napp.use(cors());\napp.use(express.json());\n\napp.get(\'/api/users\', (req, res) => {\n    res.json({ users: [] });\n});\n\napp.listen(3000, () => {\n    console.log(\'Server running on port 3000\');\n});</code></pre><h2>Middleware</h2><p>Express middleware cho phép xử lý request/response:</p><pre><code>// Authentication middleware\nconst auth = (req, res, next) => {\n    const token = req.headers.authorization;\n    if (!token) {\n        return res.status(401).json({ error: \'No token provided\' });\n    }\n    next();\n};</code></pre>',
                'tags': 'Node.js, Express, REST API, Backend, JavaScript',
                'image': 'blog_images/node_express.jpg',
            },
            {
                'title': 'CSS Grid và Flexbox: Layout hiện đại cho web',
                'summary': 'Học cách sử dụng CSS Grid và Flexbox để tạo layout responsive và hiện đại.',
                'content': '<h2>CSS Flexbox</h2><p>Flexbox cho phép tạo layout một chiều (row hoặc column):</p><pre><code>.container {\n    display: flex;\n    justify-content: space-between;\n    align-items: center;\n    flex-wrap: wrap;\n}</code></pre><h2>CSS Grid</h2><p>Grid cho phép tạo layout hai chiều:</p><pre><code>.grid-container {\n    display: grid;\n    grid-template-columns: repeat(3, 1fr);\n    grid-gap: 20px;\n    grid-template-areas:\n        "header header header"\n        "sidebar main main"\n        "footer footer footer";\n}</code></pre><h2>Responsive Design</h2><p>Sử dụng media queries để tạo layout responsive:</p><pre><code>@media (max-width: 768px) {\n    .grid-container {\n        grid-template-columns: 1fr;\n    }\n}</code></pre>',
                'tags': 'CSS, Flexbox, Grid, Layout, Responsive Design',
                'image': 'blog_images/css_grid_flexbox.jpg',
            },
            {
                'title': 'TypeScript: JavaScript với type safety',
                'summary': 'Tìm hiểu TypeScript và cách nó giúp viết code JavaScript an toàn hơn.',
                'content': '<h2>TypeScript là gì?</h2><p>TypeScript là superset của JavaScript, thêm static typing và các tính năng OOP.</p><h2>Basic Types</h2><pre><code>let name: string = "John";\nlet age: number = 25;\nlet isActive: boolean = true;\nlet hobbies: string[] = ["reading", "coding"];\nlet user: { name: string; age: number } = { name: "John", age: 25 };</code></pre><h2>Interfaces</h2><pre><code>interface User {\n    id: number;\n    name: string;\n    email: string;\n    age?: number; // Optional property\n}\n\nfunction createUser(user: User): User {\n    return user;\n}</code></pre><h2>Generics</h2><pre><code>function identity<T>(arg: T): T {\n    return arg;\n}\n\nlet output = identity<string>("hello");</code></pre>',
                'tags': 'TypeScript, JavaScript, Type Safety, Frontend',
                'image': 'blog_images/typescript.jpg',
            },
            {
                'title': 'Vue.js 3: Composition API và setup script',
                'summary': 'Khám phá Vue.js 3 với Composition API và cách viết component hiện đại.',
                'content': '<h2>Vue.js 3 Composition API</h2><p>Composition API cho phép tổ chức logic theo tính năng thay vì theo lifecycle:</p><pre><code><script setup>\nimport { ref, computed, onMounted } from \'vue\';\n\nconst count = ref(0);\nconst doubleCount = computed(() => count.value * 2);\n\nfunction increment() {\n    count.value++;\n}\n\nonMounted(() => {\n    console.log(\'Component mounted\');\n});\n</script>\n\n<template>\n    <div>\n        <p>Count: {{ count }}</p>\n        <p>Double: {{ doubleCount }}</p>\n        <button @click="increment">Increment</button>\n    </div>\n</template></code></pre><h2>Reactivity</h2><p>Vue 3 sử dụng Proxy để tạo reactivity:</p><pre><code>import { reactive } from \'vue\';\n\nconst state = reactive({\n    user: {\n        name: \'John\',\n        age: 25\n    }\n});</code></pre>',
                'tags': 'Vue.js, Composition API, Frontend, JavaScript',
                'image': 'blog_images/vue3.jpg',
            },
            {
                'title': 'MongoDB và Mongoose: Database NoSQL cho Node.js',
                'summary': 'Học cách sử dụng MongoDB với Mongoose ODM trong ứng dụng Node.js.',
                'content': '<h2>Setup MongoDB</h2><pre><code>npm install mongoose dotenv</code></pre><h2>Connection</h2><pre><code>const mongoose = require(\'mongoose\');\nrequire(\'dotenv\').config();\n\nmongoose.connect(process.env.MONGODB_URI, {\n    useNewUrlParser: true,\n    useUnifiedTopology: true\n});</code></pre><h2>Schema và Model</h2><pre><code>const userSchema = new mongoose.Schema({\n    name: {\n        type: String,\n        required: true,\n        trim: true\n    },\n    email: {\n        type: String,\n        required: true,\n        unique: true,\n        lowercase: true\n    },\n    age: {\n        type: Number,\n        min: 0\n    },\n    createdAt: {\n        type: Date,\n        default: Date.now\n    }\n});\n\nconst User = mongoose.model(\'User\', userSchema);</code></pre>',
                'tags': 'MongoDB, Mongoose, NoSQL, Node.js, Database',
                'image': 'blog_images/mongodb_mongoose.jpg',
            },
            {
                'title': 'GraphQL với Apollo Server: API hiện đại',
                'summary': 'Tìm hiểu GraphQL và cách implement với Apollo Server.',
                'content': '<h2>GraphQL là gì?</h2><p>GraphQL là query language cho API, cho phép client request chính xác dữ liệu cần thiết.</p><h2>Setup Apollo Server</h2><pre><code>npm install apollo-server graphql</code></pre><h2>Schema Definition</h2><pre><code>const typeDefs = gql`\n  type User {\n    id: ID!\n    name: String!\n    email: String!\n    posts: [Post!]!\n  }\n  \n  type Post {\n    id: ID!\n    title: String!\n    content: String!\n    author: User!\n  }\n  \n  type Query {\n    users: [User!]!\n    user(id: ID!): User\n    posts: [Post!]!\n  }\n`;</code></pre><h2>Resolvers</h2><pre><code>const resolvers = {\n  Query: {\n    users: () => User.find(),\n    user: (_, { id }) => User.findById(id),\n    posts: () => Post.find()\n  },\n  User: {\n    posts: (parent) => Post.find({ authorId: parent.id })\n  }\n};</code></pre>',
                'tags': 'GraphQL, Apollo Server, API, Backend',
                'image': 'blog_images/graphql_apollo.jpg',
            },
            {
                'title': 'Testing trong JavaScript: Jest và React Testing Library',
                'summary': 'Học cách viết test cho JavaScript và React applications.',
                'content': '<h2>Jest Framework</h2><p>Jest là testing framework phổ biến cho JavaScript:</p><pre><code>// math.test.js\nfunction sum(a, b) {\n    return a + b;\n}\n\ndescribe(\'Math functions\', () => {\n    test(\'adds 1 + 2 to equal 3\', () => {\n        expect(sum(1, 2)).toBe(3);\n    });\n    \n    test(\'adds negative numbers\', () => {\n        expect(sum(-1, -2)).toBe(-3);\n    });\n});</code></pre><h2>React Testing Library</h2><pre><code>import { render, screen, fireEvent } from \'@testing-library/react\';\nimport Counter from \'./Counter\';\n\ntest(\'renders counter\', () => {\n    render(<Counter />);\n    expect(screen.getByText(\'Count: 0\')).toBeInTheDocument();\n});\n\ntest(\'increments counter\', () => {\n    render(<Counter />);\n    fireEvent.click(screen.getByText(\'Increment\'));\n    expect(screen.getByText(\'Count: 1\')).toBeInTheDocument();\n});</code></pre>',
                'tags': 'Testing, Jest, React Testing Library, JavaScript',
                'image': 'blog_images/testing_js.jpg',
            },
            {
                'title': 'CI/CD với GitHub Actions: Tự động hóa deployment',
                'summary': 'Học cách setup CI/CD pipeline với GitHub Actions.',
                'content': '<h2>GitHub Actions Workflow</h2><p>Tạo file `.github/workflows/deploy.yml`:</p><pre><code>name: Deploy to Production\n\non:\n  push:\n    branches: [ main ]\n\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n    - uses: actions/checkout@v2\n    - name: Use Node.js\n      uses: actions/setup-node@v2\n      with:\n        node-version: \'16\'\n    - run: npm ci\n    - run: npm test\n    \n  deploy:\n    needs: test\n    runs-on: ubuntu-latest\n    steps:\n    - uses: actions/checkout@v2\n    - name: Deploy to server\n      run: |\n        echo "Deploying..."\n        # Add your deployment commands here</code></pre><h2>Environment Variables</h2><pre><code>env:\n  NODE_ENV: production\n  DATABASE_URL: ${{ secrets.DATABASE_URL }}\n  API_KEY: ${{ secrets.API_KEY }}</code></pre>',
                'tags': 'CI/CD, GitHub Actions, DevOps, Deployment',
                'image': 'blog_images/cicd_github.jpg',
            },
            {
                'title': 'Performance Optimization: Tối ưu hóa website',
                'summary': 'Các kỹ thuật tối ưu hóa performance cho website.',
                'content': '<h2>Frontend Optimization</h2><ul><li><strong>Code Splitting:</strong> Chia nhỏ bundle để load nhanh hơn</li><li><strong>Lazy Loading:</strong> Load component khi cần thiết</li><li><strong>Image Optimization:</strong> Nén và sử dụng format hiện đại (WebP)</li><li><strong>Caching:</strong> Browser caching và CDN</li></ul><h2>Backend Optimization</h2><ul><li><strong>Database Indexing:</strong> Tối ưu queries</li><li><strong>Caching:</strong> Redis, Memcached</li><li><strong>Load Balancing:</strong> Phân tải traffic</li><li><strong>Compression:</strong> Gzip, Brotli</li></ul><h2>Monitoring</h2><pre><code>// Performance monitoring\nconst observer = new PerformanceObserver((list) => {\n    for (const entry of list.getEntries()) {\n        console.log(\'Loading time:\', entry.loadEventEnd - entry.loadEventStart);\n    }\n});\nobserver.observe({ entryTypes: [\'navigation\'] });</code></pre>',
                'tags': 'Performance, Optimization, Frontend, Backend, Monitoring',
                'image': 'blog_images/performance_opt.jpg',
            }
        ]
        
        # Chỉ tạo mới nếu chưa có dữ liệu
        if existing_count == 0:
            for data in blog_data:
                BlogPost.objects.create(
                    title=data['title'],
                    summary=data['summary'],
                    content=data['content'],
                    image=data['image'],
                    tags=data['tags'],
                    created_at=timezone.now()
                )
            self.stdout.write(self.style.SUCCESS(f'Đã import {len(blog_data)} bài blog thực tế về IT!'))
        else:
            self.stdout.write(self.style.WARNING(f'Đã có {existing_count} bài blog trong database. Không import để tránh ghi đè dữ liệu hiện có.'))
            self.stdout.write(self.style.SUCCESS('Nếu muốn import lại, hãy xóa dữ liệu cũ trước.')) 