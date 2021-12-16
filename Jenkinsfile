node {
   stage('Prepare') {
      
      git url: 'https://github.com/AhmedRaies/testNA.git'
      if (!fileExists("docker-compose.yml")) {
         error('Dockerfile missing.')
      }
   }

   stage('Build') {
       
      sh "docker-compose build"
   }

   stage("Run"){
      sh "docker-compose up "
    }
}