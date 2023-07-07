node {
    stage ('Checkout') {
        cleanWs()
        checkout scm
        sh '''
            git clone --branch ${BRANCH_NAME} /Users/jkasturi/kmit
        '''
    }
    stage ('Build') {
        echo "Setup python environment"
        echo "Activate environment"
        echo "Build the code"
    }

    stage('Test') {
        echo "Runnin tests"
        sh '''
            cd kmit
            python3 -m unittest math_functions_test.MathFunctionsTest
        '''
    }  
}
