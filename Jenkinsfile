node(){
    checkout scm
withCredentials([string(credentialsId: 'dockerhub', variable: 'PASS')]) {



    stage("Build"){
       build()
    }

    stage("Test"){
            sh """
            docker login --username 209086008 --password ${PASS}
            docker pull 209086008/missions_app
            docker pull 209086008/team_app
            docker-compose up -d
            cd checking
            pip3 install requests
            test=\$(python3 test.py http://localhost:80)
            if [ \$test = "True" ]; then
                echo "Success"
                docker-compose down
            else
                echo "Failed!!"
                docker-compose down
                exit 1
            fi
            """
    }

    stage("Deploy"){
        echo "This is the deployment!!!"
    }
}

}





def build(){
    sh """
    cd teams
    docker build -t 209086008/team_app .
    cd ..
    cd missions
    docker build -t 209086008/missions_app .
    docker login --username 209086008 --password ${PASS}
    docker push 209086008/missions_app
    docker push 209086008/team_app
    """
}
