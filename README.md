# Shreyas Chaudhary

**MS-CS at California State Polytechnic University, Pomona**

![Profile Views](https://komarev.com/ghpvc/?username=shreyas463&color=blue)

## Thanks for stopping by! 👋

### I'm a Full Stack Developer

```javascript
class Shreyas {
  constructor(coffee) {
    this.name = 'Shreyas Chaudhary';
    this.pronouns = 'he' || 'him';
    this.coffee = coffee;
    this.needsCoffee = true;
    this.languages = [
      'Python', 'Java', 'C', 'JavaScript', 'SQL', 'C++', 'TypeScript', 'C#', 
      'PostgreSQL', 'Dart', 'DynamoDB', 'AWS Lambda'
    ];
    this.frameworks = [
      'PyTorch', 'Keras', 'Gen AI', 'Spark', 'Hadoop', 'Kafka', 'Azure', 'AJAX', 
      'Flask', 'OpenGL', 'React', 'NodeJS', 'Django', 'jQuery', 'AWS CDK', 'Figma', 
      'PHP', 'Pandas', 'Git', 'Linux', 'SQS', 'OpenCV', 'Redux', 'PowerBI', 'S3', 
      'FireStore', 'NextJS', 'NoSQL', 'REST', 'GraphQL', 'Heroku', 'Jenkins', 
      'MySQL', 'MongoDB', 'SNS', 'Unix', 'Agile', 'ETL', 'Three.js', 'Flutter'
    ];
    this.environments = ['Node'];
    this.libraries = [
      'Express', 'Redux', 'GraphQL', 'Apollo Server/Client', 'Axios'
    ];
    this.cssLibraries = ['Tailwind', 'Material UI', 'Bootstrap'];
    this.terminals = ['Git', 'Ubuntu'];
    this.tools = ['Github', 'Gitlab', 'Bitbucket', 'VSCode'];
  }

  giveCoffee(newCoffee) {
    this.coffee = newCoffee;
  }

  coffeeSupply() {
    if(this.coffee === null) {
      return 'Yes, please!';
    }
    return 'No, thank you';
  }
}

const hired = new Shreyas('cold brew');
